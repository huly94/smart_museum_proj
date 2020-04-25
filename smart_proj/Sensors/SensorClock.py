import logging
import smart_proj.Sensors.Sensor
import statemachine

"""@package docstring
Documentation for this module.

A sensor based on the clock. We need it to know the time, in order to turn the lights when it’s dark.

"""


class SensorClock(smart_proj.Sensors.Sensor.Sensor):
    day = statemachine.State("Morning", initial=True)
    night = statemachine.State("Night")

    day_to_night = day.to(night)
    night_to_day = night.to(day)

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def on_enter_day(self):
        self.logger.info("it's morning, new state:" + self.current_state.name)
        self.notify()

    def on_enter_night(self):
        self.logger.info(" it's night, new state:" + self.current_state.name)
        self.notify()
