import logging

import statemachine

import smart_proj.Sensors.Sensor


class SensorMobile(smart_proj.Sensors.Sensor.Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    mobile_waiting = statemachine.State('Mobile waiting', initial=True)
    signal_received = statemachine.State('Signal received')

    signal_sent = mobile_waiting.to(signal_received)
    reset = signal_received.to(mobile_waiting)

    def __init__(self):
        super().__init__()

    def on_enter_mobile_waiting(self):
        logging.info("[SENSOR MOBILE]: mobile waiting, new state" + self.current_state.name)
        self.notify()

    def on_enter_signal_received(self):
        logging.info("[SENSOR MOBILE]: received input, new state" + self.current_state.name)
        self.notify()