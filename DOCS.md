
# Deye MQTT Addon

## Overview

The Deye MQTT addon for Home Assistant allows you to connect your Deye inverter to an MQTT broker, enabling real-time monitoring and control. This addon reads data from the Deye inverter via Wifi datalogger and publishes it to the MQTT broker, making it accessible in Home Assistant and other MQTT clients.

## Configuration

To configure the Deye MQTT addon, you need to set various options in the `config.json` file. Below is a detailed explanation of each configuration option:

### Configuration Options

- **broker** (str)
  - **Description**: The IP address of the MQTT broker.
  - **Example**: `"192.168.1.1"`

- **port** (int)
  - **Description**: The port number of the MQTT broker.
  - **Example**: `1883`

- **user** (str)
  - **Description**: The username for the MQTT broker. If not used, leave it blank.
  - **Example**: `"us_1"`

- **pwd** (str)
  - **Description**: The password for the MQTT broker. If no user is used, leave it blank.
  - **Example**: `"pwdlesspwd"`

- **deye_id** (str)
  - **Description**: The ID of the Deye inverter. This ID will be used as the MQTT topic prefix. Generally, it allows the use of multiple Deye inverters at the same time.
  - **Example**: `"deye_inverter"`

- **deye_ip** (str)
  - **Description**: The IP address of the Deye inverter datalogger.
  - **Example**: `"192.168.1.1"`

- **deye_ser_nr** (int)
  - **Description**: The serial number of the Deye datalogger.
  - **Example**: `2787456322`

- **read_all_registers_period** (int)
  - **Description**: The period for reading all registers, in seconds. With this period, at least, all registers are read from the Deye inverter and published via MQTT. You can specify individual periods in the register periods section.
  - **Example**: `300`

- **reg_map** (list)
  - **Description**: Set individual reading (and automatically publishing) periods for particular registers. The registers are read from the Deye inverter and published via MQTT. This configuration consists of a list of registers and delay. The registers can contain a list of register names separated by a comma.
  - **Example**:
    ```yaml
    - register: battery_out_current, battery_out_power
      delay: 30
    - register: pv1_in_power, pv2_in_power
      delay: 300
    ```

## Installation
  1. Navigate in your Home Assistant frontend to Settings -> Add-ons -> Add-on store.
  2. Click on the "Add-on Store" tab.
  3. Click on the three dots menu in the upper right corner and select "Repositories".
  4. Add the URL of the repository (https://github.com/romanstanek81/deye_mqtt).
  5. Find the "deye mqtt" add-on and click it.
  6. Click on the "INSTALL" button.

## Usage

### Reading a register
After the addon is installed and running, it will start reading data from the Deye inverter at the configured intervals and publish this data to the MQTT broker. The registers are automatically added to your homeassitant under a name of `deye_id`_`register_name`.  Once the addon is started, all sensor configs are published and you can see them in
homeassitant -> Settings -> Devices & Services -> MQTT -> devices -> `deye_id`.

#### List of all available registers that are read
The thissupported registers are read once per `read_all_registers_period` configuration.

| Register Name | Type |
| ------------- | ---- |
| active_power_today | Float |
| batt_absorbtion_v | Float |
| batt_capacity | Int |
| batt_empty_v | Float |
| batt_equalization_v | Float |
| batt_float_v | Float |
| batt_resistance | Int |
| batt_shutdown_voltage | Float |
| batt_wake_up | Bool |
| battery_charge_today | Float |
| battery_charging_eff | Float |
| battery_corrected_ah | Int |
| battery_discharge_today | Float |
| battery_low_capacity | Int |
| battery_low_voltage | Float |
| battery_out_current | Float |
| battery_out_power | Int |
| battery_recovery_capacity | Int |
| battery_shutdown_capacity | Int |
| battery_shutdown_voltage | Float |
| battery_soc | Float |
| battery_temperature | Float |
| battery_voltage | Float |
| bms_battery_SOC | Int |
| bms_battery_alarm | Bool |
| bms_battery_current | Int |
| bms_battery_fault_location | Int |
| bms_battery_symbol_2 | Int |
| bms_battery_soh | Int |
| bms_battery_voltage | Float |
| bms_charge_current_limit | Int |
| bms_charged_voltage | Float |
| bms_discharged_voltage | Float |
| bms_discharge_current_limit | Int |
| bms_max_charge_current | Int |
| bms_max_discharge_current | Int |
| comm_address | Int |
| dc_transformer_temp | TempWithOf |
| gen_cooling_time | Float |
| gen_charge_current | Int |
| gen_charge_start_soc | Float |
| gen_charge_start_voltage | Float |
| gen_max_working_time | Float |
| gen_peak_shaving_pwr | Int |
| gen_phase_A_power | Int |
| gen_phase_A_volt | Float |
| gen_phase_B_power | Int |
| gen_phase_B_volt | Float |
| gen_phase_C_power | Int |
| gen_phase_C_volt | Float |
| gen_total_power | Int |
| generator_to_grid | Bool |
| generator_worktime_today | Float |
| grid_active_side_side_apparent_power | Int |
| grid_active_side_side_in_power | Int |
| grid_charge_current | Int |
| grid_charge_start_soc | Int |
| grid_charge_start_voltage | Float |
| grid_connection_today | Float |
| grid_high_frequency | Float |
| grid_high_voltage | Float |
| grid_in_frequency | Float |
| grid_low_frequency | Float |
| grid_low_voltage | Float |
| grid_max_output_pwr | Int |
| grid_peak_shaving_pwr | Int |
| grid_phase_A__power | Int |
| grid_phase_A_in_current | Float |
| grid_phase_A_in_power | Int |
| grid_phase_A_out_current | Float |
| grid_phase_A_out_of_grid_current | Float |
| grid_phase_A_out_of_grid_power | Int |
| grid_phase_A_volt | Float |
| grid_phase_A_volt_out | Float |
| grid_phase_AB_volt | Float |
| grid_phase_B__power | Int |
| grid_phase_B_in_current | Float |
| grid_phase_B_in_power | Int |
| grid_phase_B_out_current | Float |
| grid_phase_B_out_of_grid_current | Float |
| grid_phase_B_out_of_grid_power | Int |
| grid_phase_B_volt | Float |
| grid_phase_B_volt_out | Float |
| grid_phase_BC_volt | Float |
| grid_phase_C__power | Int |
| grid_phase_C_in_current | Float |
| grid_phase_C_in_power | Int |
| grid_phase_C_out_current | Float |
| grid_phase_C_out_of_grid_current | Float |
| grid_phase_C_out_of_grid_power | Int |
| grid_phase_C_volt | Float |
| grid_phase_C_volt_out | Float |
| grid_phase_CA_volt | Float |
| grid_total_out_of_grid_apparent_power | Int |
| grid_total_out_of_grid_power | Int |
| grid_total_power | Int |
| heatsink_temp | TempWithOf |
| inverter_out_frequency | Float |
| inverter_phase_A_out_current | Float |
| inverter_phase_A_out_power | Int |
| inverter_phase_B_out_current | Float |
| inverter_phase_B_out_power | Int |
| inverter_phase_C_out_current | Float |
| inverter_phase_C_out_power | Int |
| inverter_total_apparent_out_power | Int |
| inverter_total_out_power | Int |
| load_phase_A_current | Float |
| load_phase_A_power | Int |
| load_phase_A_volt | Float |
| load_phase_B_current | Float |
| load_phase_B_power | Int |
| load_phase_B_volt | Float |
| load_phase_C_current | Float |
| load_phase_C_power | Int |
| load_phase_C_volt | Float |
| load_total_power | Int |
| max_charge_amps | Int |
| max_discharge_amps | Int |
| max_solar_sell_pwr | Int |
| modbus_address | Int |
| output_power_factor | Float |
| pv1_current | Float |
| pv1_in_power | Int |
| pv1_volt | Float |
| pv2_current | Float |
| pv2_in_power | Int |
| pv2_volt | Float |
| rated_power | Int |
| reactive_power_today | Float |
| sell_point_t1_soc | Int |
| sell_point_t1_volts | Float |
| sell_point_t1_watts | Int |
| sell_point_t2_soc | Int |
| sell_point_t2_volts | Float |
| sell_point_t2_watts | Int |
| sell_point_t3_soc | Int |
| sell_point_t3_volts | Float |
| sell_point_t3_watts | Int |
| sell_point_t4_soc | Int |
| sell_point_t4_volts | Float |
| sell_point_t4_watts | Int |
| sell_point_t5_soc | Int |
| sell_point_t5_volts | Float |
| sell_point_t5_watts | Int |
| sell_point_t6_soc | Int |
| sell_point_t6_volts | Float |
| sell_point_t6_watts | Int |
| smart_load_open_delay | Int |
| solar_sell | Bool |
| switch_on_off | Bool |
| TEMPCO | Int |
| today_bought_from_grid | Float |
| today_from_generator | Float |
| today_from_pv | Float |
| today_from_pv_s1 | Float |
| today_from_pv_s2 | Float |
| today_sold_to_grid | Float |
| today_to_load | Float |
| ups_phase_A_power | Int |
| ups_phase_B_power | Int |
| ups_phase_C_power | Int |
| ups_total_power | Int |
| zero_export_power | Int |


### Write a value to register 
The addon also allows to write to particular registers. To do so, publish the value to the sensor with a set command.

For example, to write value 50 to `zero_export_power` register, publish message with topic "deye_inverter/zero_export_power/set" and message set to "50". To do it from linux console you can do it via the following:

```bash
mosquitto_pub -h 192.168.1.1 -t "deye_inverter/zero_export_power/set" -m "50"
```
#### Write a value to a defined register
If a register is not listed below, it can be specified by number and type in topic. Supported types are int, float, bool.

The following example writes value 0 to int register at address 172:

```bash
mosquitto_pub -h 192.168.1.1 -t "deye_inverter/172_int/set" -m "0"
```

#### Writable registers
##### Supported register types
The supported register types are listed below. Others will be added hopefully soon.

| Register type | Possible values | Example |
| ------------- | --------------- | ------- |
| Bool | 0,1 | 1 |
| Int | integer values | 12454 |
| Long | long int values | 2342342366657 |
| Float | floating point values | 1.2342 |

##### Writable registers list
In the table below is a list of all writeable registers including those which is not supported yet.

| Register Name | Type |
| ------------- | ---- |
| batt_absorbtion_v | Float |
| batt_capacity | Int |
| batt_empty_v | Float |
| batt_equalization_v | Float |
| batt_float_v | Float |
| battery_charging_eff | Int |
| battery_control_mode | Int |
| battery_low_capacity | Int |
| battery_low_voltage | Float |
| battery_recovery_capacity | Int |
| battery_restart_voltage | Float |
| battery_shutdown_capacity | Int |
| battery_shutdown_voltage | Float |
| charge_point_t1 | GridGen |
| charge_point_t2 | GridGen |
| charge_point_t3 | GridGen |
| charge_point_t4 | GridGen |
| charge_point_t5 | GridGen |
| charge_point_t6 | GridGen |
| control_mode | Int |
| gen_charge_current | Int |
| gen_charge_start_soc | Float |
| gen_charge_start_voltage | Float |
| gen_cooling_time | Float |
| gen_max_working_time | Float |
| gen_port_use | GenPortUse |
| grid_charge_current | Int |
| grid_charge_start_soc | Int |
| grid_charge_start_voltage | Float |
| grid_freq_selection | Int |
| grid_high_frequency | Float |
| grid_high_voltage | Float |
| grid_low_frequency | Float |
| grid_low_voltage | Float |
| grid_max_output_pwr | Int |
| grid_peak_shaving_pwr | Int |
| inverter_time | DeviceTime |
| max_charge_amps | Int |
| max_discharge_amps | Int |
| sell_point_t1 | Time |
| sell_point_t1_soc | Int |
| sell_point_t1_volts | Float |
| sell_point_t1_watts | Int |
| sell_point_t2 | Time |
| sell_point_t2_soc | Int |
| sell_point_t2_volts | Float |
| sell_point_t2_watts | Int |
| sell_point_t3 | Time |
| sell_point_t3_soc | Int |
| sell_point_t3_volts | Float |
| sell_point_t3_watts | Int |
| sell_point_t4 | Time |
| sell_point_t4_soc | Int |
| sell_point_t4_volts | Float |
| sell_point_t4_watts | Int |
| sell_point_t5 | Time |
| sell_point_t5_soc | Int |
| sell_point_t5_volts | Float |
| sell_point_t5_watts | Int |
| sell_point_t6 | Time |
| sell_point_t6_soc | Int |
| sell_point_t6_volts | Float |
| sell_point_t6_watts | Int |
| solar_sell | Bool |
| switch_on_off | Bool |
| tempco | Int |
| zero_export_power | Int |

## Support

For any issues or questions, please refer to the [GitHub repository](https://github.com/romanstanek81/deye_mqtt) or contact the maintainer.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/romanstanek81/deye_mqtt/blob/main/LICENSE) file for details.
