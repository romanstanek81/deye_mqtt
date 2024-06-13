
# Deye MQTT Addon

The Deye MQTT addon for Home Assistant allows you to connect your Deye inverter to an MQTT broker, enabling real-time monitoring and control. This addon reads data from the Deye inverter and publishes it to the MQTT broker, making it accessible in Home Assistant and other MQTT clients.

## Installation

1. **Download the Addon**:
   - Clone the repository or download the addon files and place them in the appropriate directory within your Home Assistant configuration.

2. **Add the Repository to Home Assistant**:
   - Go to the Supervisor panel in Home Assistant.
   - Click on the "Add-on Store" tab.
   - Click on the three dots menu in the upper right corner and select "Repositories".
   - Add the URL of your repository.

3. **Install the Addon**:
   - Find the Deye MQTT addon in the list of available addons.
   - Click on it and then click on the "Install" button.

4. **Configure the Addon**:
   - Once installed, go to the addon configuration page.
   - Fill in the configuration options as described in the [DOCS.md](./DOCS.md).

5. **Start the Addon**:
   - After configuring, click on the "Start" button to launch the addon.

6. **Check the Logs**:
   - Monitor the logs to ensure the addon is connecting to the MQTT broker and reading data from the Deye inverter correctly.

## Configuration Options

Refer to the [DOCS.md](./DOCS.md) for detailed configuration options.

## Usage

After the addon is installed and running, it will start reading data from the Deye inverter at the configured intervals and publish this data to the MQTT broker. You can then create sensors in Home Assistant to display this data.

### Example Sensor Configuration in Home Assistant

Add the following to your `configuration.yaml` to create sensors for the data published by the Deye MQTT addon:

```yaml
sensor:
  - platform: mqtt
    name: "Battery Out Current"
    state_topic: "deye_inverter/battery_out_current"
  - platform: mqtt
    name: "Battery Out Power"
    state_topic: "deye_inverter/battery_out_power"
  - platform: mqtt
    name: "PV1 In Power"
    state_topic: "deye_inverter/pv1_in_power"
  - platform: mqtt
    name: "PV2 In Power"
    state_topic: "deye_inverter/pv2_in_power"
```

Replace `"deye_inverter"` with your actual `deye_id` if it is different.

## Support

For any issues or questions, please refer to the [GitHub repository](https://github.com/your-repository) or contact the maintainer.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/your-repository/LICENSE) file for details.
