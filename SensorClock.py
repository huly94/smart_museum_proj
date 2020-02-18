from Sensor import Sensor
from statemachine import State


class SensorClock(Sensor):
    day = State("Morning", initial=True)
    night = State("Night")

    day_to_night = day.to(night)
    night_to_day = night.to(day)

    def __init__(self):
        super().__init__()

    def on_enter_day(self):
        print("it's morning, new state:", self.current_state.name)
        self.notify()

    def on_enter_night(self):
        print("it's night, new state:", self.current_state.name)
        self.notify()
