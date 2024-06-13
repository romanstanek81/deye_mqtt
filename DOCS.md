
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

1. **Download the Addon**:
   - Clone the repository or download the addon files and place them in the appropriate directory within your Home Assistant configuration.

2. **Add the Repository to Home Assistant**:
   - Go to the Supervisor panel in Home Assistant.
   - Click on the "Add-on Store" tab.
   - Click on the three dots menu in the upper right corner and select "Repositories".
   - Add the URL of the repository.

3. **Install the Addon**:
   - Find the Deye MQTT addon in the list of available addons.
   - Click on it and then click on the "Install" button.

4. **Configure the Addon**:
   - Once installed, go to the addon configuration page.
   - Fill in the configuration options as described above.

5. **Start the Addon**:
   - After configuring, click on the "Start" button to launch the addon.

6. **Check the Logs**:
   - Monitor the logs to ensure the addon is connecting to the MQTT broker and reading data from the Deye inverter correctly.

## Usage

### Reading a register
After the addon is installed and running, it will start reading data from the Deye inverter at the configured intervals and publish this data to the MQTT broker. The registers are automatically added to your homeassitant under a name of `deye_id`_`register_name`

### Write a value to register 
The addon also allows to write to particular registers. To do so, publish the value to the sensor with a set command.

For example, to write value 50 to `zero_export_power` register, publish message with topic "deye_inverter/zero_export_power/set" and message set to "50". To do it from linux console you can do it via the following:

```bash
mosquitto_pub -h 192.168.1.110 -t "deye_inverter/zero_export_power/set" -m "50"
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
| inverter_time | DeviceTimeWriteable |
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

For any issues or questions, please refer to the [GitHub repository](https://github.com/your-repository) or contact the maintainer.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/your-repository/LICENSE) file for details.