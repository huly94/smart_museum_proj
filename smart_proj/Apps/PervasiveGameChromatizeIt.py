import logging
import statemachine

import smart_proj.Sensors.Sensor
import smart_proj.Apps.Observer

"""@package docstring
Documentation for this module.

pervasive game “chromatize it!”: In an area there are three light sources colored of different colors
, a visitor through a device pick one color that uses to paint a smart wall
"""


class PervasiveGameChromatizeIt(smart_proj.Apps.Observer.Observer):
    wait = statemachine.State('Wait', initial=True)
    blue_taken = statemachine.State('Blue taken')
    red_taken = statemachine.State('Red taken')
    green_taken = statemachine.State('Green taken')
    wall_green = statemachine.State('Wall painted green')
    wall_blue = statemachine.State('Wall painted blue')
    wall_red = statemachine.State('Wall painted red')

    set_color_blue = wait.to(blue_taken) | red_taken.to(blue_taken) | green_taken.to(blue_taken)
    set_color_red = wait.to(red_taken) | blue_taken.to(red_taken) | green_taken.to(red_taken)
    set_color_green = wait.to(green_taken) | blue_taken.to(green_taken) | red_taken.to(green_taken)

    paint_wall_red = red_taken.to(wall_red) | wall_red.to(wall_red)
    paint_wall_green = green_taken.to(wall_green) | wall_green.to(wall_green)
    paint_wall_blue = blue_taken.to(wall_blue) | wall_blue.to(wall_blue)

    restart = wall_red.to(wait) | wall_green.to(wait) | wall_blue.to(wait)

    actuator_mobile = None
    actuator_wall = None
    user = None
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def set_user(self, u):
        self.user = u

    def attach(self, actuator):
        actuator_name = actuator.__str__()
        if actuator_name[0:actuator_name.index("(")] == "ActuatorMobile":
            self.actuator_mobile = actuator
        elif actuator_name[0:actuator_name.index("(")] == "ActuatorWall":
            self.actuator_wall = actuator

    def on_set_color_blue(self):
        self.logger.info("New State: blue")
        self.actuator_mobile.turn_on()

    def on_set_color_red(self):
        self.logger.info("New State: red")
        self.actuator_mobile.turn_on()

    def on_set_color_green(self):
        self.logger.info("New State: green")
        self.actuator_mobile.turn_on()

    def on_paint_wall_red(self):
        self.logger.info("New State: wall red")
        self.actuator_wall.turn_on()

    def on_paint_wall_blue(self):
        self.logger.info("New State: wall blue")
        self.actuator_wall.turn_on()

    def on_paint_wall_green(self):
        self.logger.info("New State: wall blue")
        self.actuator_wall.turn_on()

    def on_restart(self):
        self.logger.info("New State: Wait")

        self.actuator_wall.turn_off()
        self.actuator_mobile.turn_off()
        # when i turn the game off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        self.logger.info("ChromatizeIt received a new sensor value:" + subject.current_state.name)
        if subject.user == self.user:

            if "Blue" == subject.current_state.name:
                self.set_color_blue()

            elif "Red" == subject.current_state.name:
                self.set_color_red()

            elif "Green" == subject.current_state.name:
                self.set_color_green()

            elif "Detected" == subject.current_state.name:
                if "Blue taken" == self.current_state.name or "Wall painted blue" == self.current_state.name:
                    self.paint_wall_blue()
                elif "Red taken" == self.current_state.name or "Wall painted red" == self.current_state.name:
                    self.paint_wall_red()
                elif "Green taken" == self.current_state.name or "Wall painted green" == self.current_state.name:
                    self.paint_wall_green()
                else:
                    pass

            elif "Not Detected" == subject.current_state.name:
                if "Wall painted blue" == self.current_state.name or "Wall painted red" == self.current_state.name or "Wall painted green" == self.current_state.name:
                    self.restart()
