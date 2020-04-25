import logging

import statemachine

import smart_proj.Sensors.Sensor

"""@package docstring
Documentation for this module.

A SparkFun RGB Light Sensor that detect the color coming out from a light source
"""


class SensorColors(smart_proj.Sensors.Sensor.Sensor):
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
        self.logger = logging.getLogger(self.__class__.__name__)

    def on_enter_blue(self):
        self.logger.info("Color detected, new state:" + self.current_state.name)
        self.notify()

    def on_enter_red(self):
        self.logger.info("Color detected, new state:" + self.current_state.name)
        self.notify()

    def on_enter_green(self):
        self.logger.info("Color detected, new state:" + self.current_state.name)
        self.notify()

    def on_enter_off(self):
        self.logger.info("No color detected, new state:" + self.current_state.name)
        self.notify()
