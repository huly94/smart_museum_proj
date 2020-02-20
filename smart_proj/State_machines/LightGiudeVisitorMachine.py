from statemachine import State

from smart_proj.Sensors.Sensor import Sensor
from smart_proj.State_machines.Observer import Observer


class LightGuideVisitorMachine(Observer):
    colored_light_off_on_a_related_painting = State('Colored light off', initial=True)
    colored_light_on_on_a_related_painting = State('Colored light on')

    switch_on_colored_light = colored_light_off_on_a_related_painting.to(colored_light_on_on_a_related_painting)
    switch_off_light = colored_light_on_on_a_related_painting.to(colored_light_off_on_a_related_painting)

    actuator = None

    def attach_lights(self, light):
        self.actuator = light

    def on_switch_on_colored_light(self):
        print("Accendi luce colorata su un altro dipinto")
        self.actuator.turn_on()

    def on_switch_off_light(self):
        print("Switch off light")
        self.actuator.turn_off()

    def update(self, subject: Sensor):
        print("AudioMusic received new sensor value", subject.current_state.name)
        if "Mobile waiting" == subject.current_state.name:
            if "Colored light off" == self.current_state.name:
                pass
            else:
                self.switch_off_light()
        if "Signal received" == subject.current_state.name:
            if "Colored light off" == self.current_state.name:
                self.switch_on_colored_light()
            else:
                pass