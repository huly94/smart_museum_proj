import logging
import smart_proj.Sensors.Sensor
import statemachine


class SensorClock(smart_proj.Sensors.Sensor.Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    day = statemachine.State("Morning", initial=True)
    night = statemachine.State("Night")

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
