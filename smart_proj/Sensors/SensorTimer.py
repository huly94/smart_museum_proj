import logging
import statemachine
import smart_proj.Sensors.Sensor


class SensorTimer(smart_proj.Sensors.Sensor.Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    timer_waiting = statemachine.State('Timer waiting', initial=True)
    timer_expired = statemachine.State('Timer expired')

    end_timer = timer_waiting.to(timer_expired)
    reset = timer_expired.to(timer_waiting)

    def __init__(self):
        super().__init__()

    def on_enter_timer_expired(self):
        logging.info("[SENSOR TIMER]: timer expired, new state" + self.current_state.name)
        self.notify()

    def on_enter_timer_waiting(self):
        logging.info("[SENSOR TIMER]: timer reset, new state" + self.current_state.name)
        self.notify()


