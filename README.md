
# Deye MQTT Addon

The Deye MQTT addon for Home Assistant allows you to connect your Deye inverter to an MQTT broker, enabling real-time monitoring and control. This addon reads data from the Deye inverter and publishes it to the MQTT broker, making it accessible in Home Assistant and other MQTT clients.

## Installation
  1. Navigate in your Home Assistant frontend to Settings -> Add-ons -> Add-on store.
  2. Click on the "Add-on Store" tab.
  3. Click on the three dots menu in the upper right corner and select "Repositories".
  4. Add the URL of the repository (https://github.com/romanstanek81/deye_mqtt).
  5. Find the "deye mqtt" add-on and click it.
  6. Click on the "INSTALL" button.

## Configuration Options

Refer to the [DOCS.md](https://github.com/romanstanek81/deye_mqtt/blob/main/DOCS.md) for detailed configuration options.

## Usage

After the addon is installed and running, it will start reading data from the Deye inverter at the configured intervals and publish this data to the MQTT broker. The configuration of sensors are published via MQTT config message so related sensors are added to homeassistant automatically.

## Support

For any issues or questions, please refer to the [GitHub repository](https://github.com/romanstanek81/deye_mqtt) or contact the maintainer.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/romanstanek81/deye_mqtt/blob/main/LICENSE) file for details.
