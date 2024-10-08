from deye_controller.modbus.protocol import *
from deye_controller import HoldingRegisters, WritableRegisters
import json
import time
import paho.mqtt.client as mqtt
from deyeoper import DeyeInverter
from register_sets import read_regs_supported, read_write_reg_map


with open('/data/options.json', 'r') as file:
    config = json.load(file)

broker=config.get('broker')
port=config.get('port')
user=config.get('user')
pwd=config.get('pwd')
deye_id=config.get('deye_id')
deye_ip=config.get('deye_ip')
deye_ser_nr=config.get('deye_ser_nr')
read_all_registers_period=config.get('read_all_registers_period')

reg_map_with_spec_delays=config.get('reg_map')

sw_version = "2024.6.7" # basically it is a date
deye_model = "SUN-12K-SG04LP3-EU"

inv = DeyeInverter(deye_ip, deye_ser_nr)

read_regs_desc = [instance.description.lower() for instance in read_regs_supported]
read_regs_desc_to_inst = {instance.description.lower():instance  for instance in read_regs_supported}


def get_discovery_msgs(regs):
    dev_classes_mapping = {"V": "voltage",
                        "W": "power",
                        "%": "battery",
                        "A": "current",
                        "kWh": "energy",
                        "°C": "temperature",
                        }
    out = {}
    for i in regs:
        item = i.description.lower()
        discovery_msg = {"name":  item,
                         "uniq_id":  "deye_inverter_"+item,
                         "state_class": "measurement", #TODO
                         "state_topic": deye_id + "/" + item + "/state",
                         "avty_t": deye_id + "/status",
                         "value_template": "{{ value_json.value }}",
                         "device": { "ids": "deye_00001" ,
                                    "sw": sw_version,
                                    "mdl": deye_model,
                                    "mf": "DEYE",
                                    "name": deye_id }}
        if item in read_write_reg_map:
            discovery_msg["command_topic"] = deye_id + "/" + item + "/set"

        if i.suffix != "":
            discovery_msg["unit_of_measurement"] = i.suffix
            if i.suffix in dev_classes_mapping:
                discovery_msg['device_class'] = dev_classes_mapping[i.suffix]
        out[item] = json.dumps(discovery_msg)
    return out


def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    msg=message.payload.decode()
    t_parts=message.topic.split("/")
    if t_parts[0] == deye_id and t_parts[2] == 'set':
        reg_name = t_parts[1]
        if reg_name in read_write_reg_map:
            wr = read_write_reg_map[reg_name]
        else:
            # custom: like '172_int' register 172, type IntWritable
            parts=reg_name.split("_")
            if len(parts) != 2:
                print("Bad reg_name:"+reg_name)
                return
            else:
                try:
                    reg_nr = int(parts[0])
                except Exception as e:
                    print("register number is not a number")
                    return

                if parts[1] == 'int':
                    wr=IntWritable(reg_nr)
                elif parts[1] == 'float':
                    wr=FloatWritable(reg_nr)
                elif parts[1] == 'bool':
                    wr=BoolWritable(reg_nr)
                else:
                    return

        if isinstance(wr, BoolWritable):
            if msg == '1' or msg.lower() == "true" or msg.lower() == "active":
                val = True
            elif msg == '0' or msg.lower() == "false" or msg.lower() == "inactive":
                val = False
            else:
                # TODO LOG
                print("bad bool value {}. e: {}".format(msg, e))
                return
        elif isinstance(wr, FloatWritable):
            try:
                val = float(msg)
            except Exception as e:
                # TODO LOG
                print("bad float value {}. e: {}".format(msg, e))
                return
        elif isinstance(wr, IntWritable):
            try:
                val = int(msg)
            except Exception as e:
                # TODO LOG
                print("bad int value {}. e: {}".format(msg, e))
                return
        wr.set(val)
        inv.write(wr)


def publish_data(data):
    for i in data:
        item = i.lower()
        val = str(data[i])
        if item in read_regs_desc_to_inst:
            r = read_regs_desc_to_inst[item]
            if isinstance(r, BoolType):
                if data[i] == 'Inactive':
                    val = "0"
                else:
                    val = "1"
            
        client.publish(deye_id + "/" + i.lower() + "/state", "{ \"value\": \"" + val+"\"}", retain=True)    

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    dis_msgs = get_discovery_msgs(read_regs_supported)

    client.publish(deye_id + "/status","online",  qos=1, retain=True)
    for m in dis_msgs:
        # remove it before run ?
        #client.publish("homeassistant/sensor/" + m + "/config", "")
        client.publish("homeassistant/sensor/" + m + "/config", dis_msgs[m], retain=True)

    client.subscribe(deye_id + "/+/set")

client = mqtt.Client(deye_id)

client.on_connect = on_connect
client.on_message = on_message
if user != "":
    client.username_pw_set(username=user,password=pwd)

client.will_set(deye_id + "/status","offline", qos=1, retain=False)
client.connect(broker)
client.loop_start()


for i in read_regs_desc:
    inv.add_reg_to_read(i,read_all_registers_period)



for i in reg_map_with_spec_delays:
    if "delay" not in i or "registers" not in i:
        continue
    delay = int(i["delay"])
    reg_names = [x.strip() for x in i['registers'].split(",")]
    for r in reg_names:
        inv.add_reg_to_read(r, delay)

inv.reg_cb(publish_data)
inv.start()

while True:
    time.sleep(1)

