import logging
import statemachine

import smart_proj.Sensors.Sensor
import smart_proj.State_machines.Observer


class PervasiveGameChromatizeIt(smart_proj.State_machines.Observer.Observer):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
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

    def attach_mobile(self, mobile):
        self.actuator_mobile = mobile


    def attach_wall(self, wall):
        self.actuator_wall = wall

    def on_set_color_blue(self):
        logging.info("New State: blue")
        self.actuator_mobile.turn_on()

    def on_set_color_red(self):
        logging.info("New State: red")
        self.actuator_mobile.turn_on()

    def on_set_color_green(self):
        logging.info("New State: green")
        self.actuator_mobile.turn_on()

    def on_paint_wall_red(self):
        logging.info("New State: wall red")
        self.actuator_wall.turn_on()

    def on_paint_wall_blue(self):
        logging.info("New State: wall blue")
        self.actuator_wall.turn_on()

    def on_paint_wall_green(self):
        logging.info("New State: wall blue")
        self.actuator_wall.turn_on()

    def on_restart(self):
        logging.info("New State: Wait")
        self.actuator_wall.turn_off()
        self.actuator_mobile.turn_off()

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("ChromatizeIt received a new sensor value:" + subject.current_state.name)

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




