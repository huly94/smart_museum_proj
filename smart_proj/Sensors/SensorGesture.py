from statemachine import State

from smart_proj.Sensors.Sensor import Sensor


class SensorGesture(Sensor):
    not_detected = State('Not Detected', initial= True)
    detected = State('Detected')

    gesture_detected = not_detected.to(detected) | detected.to(detected)
    no_gesture = detected.to(not_detected)

    def __init__(self):
        super().__init__()

    def on_enter_not_detected(self):
        print("No gesture detected, new state:", self.current_state.name)
        self.notify()

    def on_enter_detected(self):
        print("Gesture detected, new state:", self.current_state.name)
        self.notify()