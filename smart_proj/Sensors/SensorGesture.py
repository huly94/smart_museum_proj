import logging
import statemachine
import smart_proj.Sensors.Sensor
"""@package docstring
Documentation for this module.

a motion sensor that detects when a visitor 
pass the paint on the smart wall
"""


class SensorGesture(smart_proj.Sensors.Sensor.Sensor):
    not_detected = statemachine.State('Not Detected', initial= True)
    detected = statemachine.State('Detected')

    gesture_detected = not_detected.to(detected) | detected.to(detected)
    no_gesture = detected.to(not_detected)

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def on_enter_not_detected(self):
        self.logger.info("No gesture detected, new state:" + self.current_state.name)
        self.notify()

    def on_enter_detected(self):
        self.logger.info("Gesture detected, new state:" + self.current_state.name)
        self.notify()