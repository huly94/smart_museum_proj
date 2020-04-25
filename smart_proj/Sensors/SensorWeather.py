import logging
import statemachine
import smart_proj.Sensors.Sensor

"""@package docstring
Documentation for this module.

a PWS100 sensor that detects the weather in order to turn on or off the lights
"""


class SensorWeather(smart_proj.Sensors.Sensor.Sensor):
    sunny = statemachine.State('Sunny', initial=True)
    cloud = statemachine.State('Cloud')

    bad_weather = sunny.to(cloud)
    good_weather = cloud.to(sunny)

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def on_enter_cloud(self):
        self.logger.info("Clouds arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_sunny(self):
        self.logger.info("Sun arrived, new state:" + self.current_state.name)
        self.notify()
