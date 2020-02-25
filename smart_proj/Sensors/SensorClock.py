import logging

from smart_proj.Sensors.Sensor import Sensor
from statemachine import State


class SensorClock(Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    day = State("Morning", initial=True)
    night = State("Night")

    day_to_night = day.to(night)
    night_to_day = night.to(day)

    def __init__(self):
        super().__init__()

    def on_enter_day(self):
        logging.info("[SENSOR CLOCK]: it's morning, new state:" + self.current_state.name)
        self.notify()

    def on_enter_night(self):
        logging.info("[SENSOR CLOCK]: it's night, new state:" + self.current_state.name)
        self.notify()
