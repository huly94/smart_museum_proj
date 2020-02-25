import logging

from statemachine import State

from smart_proj.Sensors.Sensor import Sensor


class SensorColors(Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    off = State('Off', initial=True)
    blue = State('Blue')
    red = State('Red')
    green = State('Green')

    blue_detected = off.to(blue) | red.to(blue) | green.to(blue)
    red_detected = off.to(red) | blue.to(red) | green.to(red)
    green_detected = off.to(green) | red.to(green) | blue.to(green)
    no_color = blue.to(off) | red.to(off) | green.to(off)

    def __init__(self):
        super().__init__()

    def on_enter_blue(self):
        logging.info("[SENSOR COLOR]: Color detected, new state:" + self.current_state.name)
        self.notify()

    def on_enter_red(self):
        logging.info("[SENSOR COLOR]: Color detected, new state:" + self.current_state.name)
        self.notify()

    def on_enter_green(self):
        logging.info("[SENSOR COLOR]: Color detected, new state:" + self.current_state.name)
        self.notify()

    def on_enter_off(self):
        logging.info("[SENSOR COLOR]: No color detected, new state:" + self.current_state.name)
        self.notify()
