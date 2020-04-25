import logging
import statemachine
import smart_proj.Sensors.Sensor

"""@package docstring
Documentation for this module.

This sensor is triggered at the expiration of a simple timer. 
We need it in order to provide further information about a work if the visitor, 
at the end of the track, wants to know more about that particular work.
"""


class SensorTimer(smart_proj.Sensors.Sensor.Sensor):
    timer_waiting = statemachine.State('Timer waiting', initial=True)
    timer_expired = statemachine.State('Timer expired')

    end_timer = timer_waiting.to(timer_expired)
    reset = timer_expired.to(timer_waiting)

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def on_enter_timer_expired(self):
        self.logger.info("timer expired, new state" + self.current_state.name)
        self.notify()

    def on_enter_timer_waiting(self):
        self.logger.info("timer reset, new state" + self.current_state.name)
        self.notify()
