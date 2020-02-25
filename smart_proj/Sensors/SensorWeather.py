import logging

from statemachine import State
from smart_proj.Sensors.Sensor import Sensor


class SensorWeather(Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    sunny = State('Sunny', initial=True)
    cloud = State('Cloud')

    bad_weather = sunny.to(cloud)
    good_weather = cloud.to(sunny)

    def __init__(self):
        super().__init__()

    def on_enter_cloud(self):
        logging.info("[SENSOR WEATHER]: Clouds arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_sunny(self):
        logging.info("[SENSOR WEATHER]: Sun arrived, new state:" + self.current_state.name)
        self.notify()
