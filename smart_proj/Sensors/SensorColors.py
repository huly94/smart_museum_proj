import logging

import statemachine

import smart_proj.Sensors.Sensor


class SensorColors(smart_proj.Sensors.Sensor.Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    off = statemachine.State('Off', initial=True)
    blue = statemachine.State('Blue')
    red = statemachine.State('Red')
    green = statemachine.State('Green')

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
