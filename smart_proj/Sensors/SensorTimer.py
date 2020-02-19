from statemachine import State

from smart_proj.Sensors.Sensor import Sensor


class SensorTimer(Sensor):
    timer_waiting = State('Timer waiting', initial=True)
    timer_expired = State('Timer expired')

    end_timer = timer_waiting.to(timer_expired)
    reset = timer_expired.to(timer_waiting)

    def __init__(self):
        super().__init__()

    def on_enter_timer_expired(self):
        print("timer expired, new state", self.current_state.name)
        self.notify()

    def on_enter_timer_waiting(self):
        print("timer reset, new state", self.current_state.name)
        self.notify()


