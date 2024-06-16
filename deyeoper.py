from deye_controller import HoldingRegisters, WritableRegisters
from pysolarmanv5 import PySolarmanV5, NoSocketAvailableError
import time
#from cyclic_timer import CyclicTimer
from deye_controller.utils import group_registers, map_response
import threading

class DeyeInverter:
    def __init__(self, ip, serId) -> None:
        self._ip = ip
        self._ser_id = serId
        self._inv = None
        self._regs_to_read = {}
        self._regs_to_read_last_times = {}
        #self._regs_to_read = ['BMSBatteryCapacity', 'BMSBatteryVoltage', 'BMSBatteryCurrent']
        self._regs_values = {}
        self._ct = None
        self._data_lock = threading.Lock()
        self._op_lock = threading.Lock()
        self._timer_thread = None
        self._cb = None
        pass

    def reg_cb(self, cb):
        self._cb = cb
    
    def add_reg_to_read(self, reg_name, delay_sec):
        if delay_sec not in self._regs_to_read:
            self._regs_to_read[delay_sec] = []
            self._regs_to_read_last_times[delay_sec] = 0

        r = [attr for attr in HoldingRegisters.__dict__.items() if not attr[0].startswith('__') and attr[0] != 'as_list' and attr[1].description.lower()==reg_name]
        if len(r) == 1:
            print("adding {} for {}".format(r[0][1].description, delay_sec))
            self._regs_to_read[delay_sec].append(r[0][1])

    def get_values(self):
        self._data_lock.acquire()
        values = self._regs_values
        self._data_lock.release()
        return values

    def start(self):
        self._timer_thread = threading.Thread(target=self.loop)
        self._timer_thread.daemon = True
        self._timer_thread.start()

    def loop(self):
        while True:
            t = int(time.time())
            try:
                for i in self._regs_to_read:
                    if i not in self._regs_to_read_last_times or \
                        t - self._regs_to_read_last_times[i] > i:
                        self._regs_to_read_last_times[i] = t
                        self._read_registers(self._regs_to_read[i])
            except Exception as e:
                print ("exception in loop: {}".format(e))
                pass
            time.sleep(1)

    def _read_registers(self, regs):
        groups = group_registers(regs)
        for group in groups:
            def op():
                act_read_regs = {}
                res = self._inv.read_holding_registers(group.start_address, group.len)
                map_response(res, group)
                self._data_lock.acquire()
                for reg in group:
                    self._regs_values[reg.description.title()] = reg.format()
                    act_read_regs[reg.description.title()] = reg.format()
                self._data_lock.release()
                if self._cb:
                    self._cb(act_read_regs)
                return None
            self._do_inv_oper(op)
        self._inv_disconnect()


    def _inv_disconnect(self):
        if self._inv:
            self._inv.disconnect()
            self._inv = None

    def __del__(self):
        self._inv_disconnect()

    def _connect_if_needed(self):
        cnt = 0
        while cnt < 5: 
            try:
                if self._inv is None:
                    self._inv = PySolarmanV5(self._ip, self._ser_id, socket_timeout=5)
                    return
            except Exception as e:
                print("failed to connect {}, {}".format(self._ip, self._ser_id))
                time.sleep(1)
                pass
            cnt = cnt + 1
            
    def read(self, register):
        def op():
            res = self._inv.read_holding_registers(register.address, register.len)
            register.value = res[0] if register.len == 1 else res
            return register            
        return self._do_inv_oper(op)

    def write(self, register):
        def op():
            res = self._inv.write_multiple_holding_registers(register.address, [register.modbus_value])
            return res
        return self._do_inv_oper(op)

    def _do_inv_oper(self, oper_cb):
        self._op_lock.acquire()
        self._connect_if_needed()
        max_try = 5
        while (max_try > 0):
            try:
                res = oper_cb()
                self._op_lock.release()
                return res
            except Exception as e:
                self._inv_disconnect()
                self._connect_if_needed()
                max_try = max_try - 1
                if max_try == 0:
                    print("Op failed 5 timer in a row. {}".format(e))

        self._op_lock.release()
        return None
