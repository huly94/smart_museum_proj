import logging
import statemachine
import smart_proj.Sensors.Sensor


class SensorGesture(smart_proj.Sensors.Sensor.Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    not_detected = statemachine.State('Not Detected', initial= True)
    detected = statemachine.State('Detected')

    gesture_detected = not_detected.to(detected) | detected.to(detected)
    no_gesture = detected.to(not_detected)

    def __init__(self):
        super().__init__()

    def on_enter_not_detected(self):
        logging.info("[SENSOR GESTURE]:No gesture detected, new state:" + self.current_state.name)
        self.notify()

    def on_enter_detected(self):
        logging.info("[SENSOR GESTURE]Gesture detected, new state:" + self.current_state.name)
        self.notify()