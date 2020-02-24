from statemachine import State

from smart_proj.Sensors.Sensor import Sensor
from smart_proj.State_machines.Observer import Observer


class PervasiveGameChromatizeIt(Observer):
    wait = State('Wait', initial=True)
    blue_taken = State('Blue taken')
    red_taken = State('Red taken')
    green_taken = State('Green taken')
    wall_green = State('Wall painted green')
    wall_blue = State('Wall painted blue')
    wall_red = State('Wall painted red')

    set_color_blue = wait.to(blue_taken) | red_taken.to(blue_taken) | green_taken.to(blue_taken)
    set_color_red = wait.to(red_taken) | blue_taken.to(red_taken) | green_taken.to(red_taken)
    set_color_green = wait.to(green_taken) | blue_taken.to(green_taken) | red_taken.to(green_taken)

    paint_wall_red = red_taken.to(wall_red) | wall_red.to(wall_red)
    paint_wall_green = green_taken.to(wall_green) | wall_green.to(wall_green)
    paint_wall_blue = blue_taken.to(wall_blue) | wall_blue.to(wall_blue)

    actuator_mobile = None
    actuator_wall = None

    def attach_mobile(self, mobile):
        self.actuator_mobile = mobile

    def attach_wall(self, wall):
        self.actuator_wall = wall

    def on_set_color_blue(self):
        print("blue")
        self.actuator_mobile.turn_on()

    def on_set_color_red(self):
        print("red")
        self.actuator_mobile.turn_on()

    def on_set_color_green(self):
        print("green")
        self.actuator_mobile.turn_on()

    def on_paint_wall_red(self):
        print("wall red")
        self.actuator_wall.turn_on()

    def on_paint_wall_blue(self):
        print("wall blue")
        self.actuator_wall.turn_on()

    def on_paint_wall_green(self):
        print("wall blue")
        self.actuator_wall.turn_on()

    def update(self, subject: Sensor):
        print("ChromatizeIt received a new sensor value", subject.current_state.name)
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




