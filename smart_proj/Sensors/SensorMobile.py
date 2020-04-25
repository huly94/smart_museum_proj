import logging

import statemachine

import smart_proj.Sensors.Sensor

"""@package docstring
Documentation for this module.

This sensor is triggered by the pushing on a button (placed or in a mobile application or on the audio guide itself), 
when a visitor need suggestions on works related to the one is currently watching, 
in this case a colored light guide him on other works 
"""


class SensorMobile(smart_proj.Sensors.Sensor.Sensor):
    mobile_waiting = statemachine.State('Mobile waiting', initial=True)
    signal_received = statemachine.State('Signal received')

    signal_sent = mobile_waiting.to(signal_received)
    reset = signal_received.to(mobile_waiting)

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def on_enter_mobile_waiting(self):
        self.logger.info("mobile waiting, new state" + self.current_state.name)
        self.notify()

    def on_enter_signal_received(self):
        self.logger.info("received input, new state" + self.current_state.name)
        self.notify()
