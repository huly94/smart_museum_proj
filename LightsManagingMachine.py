from Observer import Observer
from Sensor import Sensor
from statemachine import StateMachine, State


class LightsManagingMachine(Observer):
    lights_off = State('Lights off', initial=True)
    lights_on_for_visitors = State('Lights on for visitors')
    lights_on_for_clouds = State('Lights on for clouds')
    lights_on_for_night = State('Lights on for night')

    turn_the_lights_on_visitor = lights_off.to(lights_on_for_visitors)
    turn_the_lights_off_visitor = lights_on_for_visitors.to(lights_off)
    turn_the_lights_on_clouds = lights_off.to(lights_on_for_clouds)
    turn_the_lights_off_clouds = lights_on_for_clouds.to(lights_off)
    turn_the_lights_on_night = lights_off.to(lights_on_for_night)
    turn_the_lights_off_night = lights_on_for_night.to(lights_off)

    actuator = None

    def attach_lights(self, lights):
        self.actuator = lights

    def on_turn_the_lights_on_visitor(self):
        print("luci accese per visitatore")
        self.actuator.turn_on()

    def on_turn_the_lights_off_visitor(self):
        print("luci spente per visitatore")
        self.actuator.turn_off()

    def on_turn_the_lights_on_clouds(self):
        print("luci accese per nuvole")
        self.actuator.turn_on()

    def on_turn_the_lights_off_clouds(self):
        print("luci spente per nuvole")
        self.actuator.turn_off()

    def on_turn_the_lights_on_night(self):
        print("luci accese notte")
        self.actuator.turn_on()

    def on_turn_the_lights_off_night(self):
        print("luci spente")
        self.actuator.turn_off()

    def update(self, subject: Sensor):
        print("LightsManaging received new sensor value", subject.current_state.name)
        if 'Empty' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                pass
            else:
                self.turn_the_lights_off_visitor()

        elif 'Non Empty' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                self.turn_the_lights_on_visitor()
            else:
                pass

        elif 'Sunny' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                pass
            else:
                self.turn_the_lights_off_clouds()

        elif 'Cloud' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                self.turn_the_lights_on_clouds()
            else:
                pass

        elif 'Morning' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                pass
            else:
                self.turn_the_lights_off_night()

        elif 'Night' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                self.turn_the_lights_on_night()
            else:
                pass











