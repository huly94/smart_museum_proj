import logging

import statemachine

import smart_proj.Sensors.Sensor
import smart_proj.Apps.App

"""@package docstring
Documentation for this module.

A colored light guide the visitor to works related to the current one
"""


class LightGuideVisitorMachine(smart_proj.Apps.App.App):
    colored_light_off_on_a_related_painting = statemachine.State('Colored light off', initial=True)
    colored_light_on_on_a_related_painting = statemachine.State('Colored light on')

    switch_on_colored_light = colored_light_off_on_a_related_painting.to(colored_light_on_on_a_related_painting)
    switch_off_light = colored_light_on_on_a_related_painting.to(colored_light_off_on_a_related_painting)

    actuator = None

    user = None
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def dependencies_sensors(self) -> []:
        import smart_proj.Sensors.SensorMobile
        return [smart_proj.Sensors.SensorMobile.SensorMobile]

    def dependencies_actuators(self) -> []:
        import smart_proj.Actuators.ActuatorLights
        return [smart_proj.Actuators.ActuatorLights.ActuatorLights]

    def set_user(self, u):
        self.user = u

    def attach(self, light):
        self.actuator = light

    def on_switch_on_colored_light(self):
        self.logger.info("Accendi luce colorata su un altro dipinto")
        self.actuator.turn_on()

    def on_switch_off_light(self):
        self.logger.info("Switch off light")
        self.actuator.turn_off()
        # when i turn the lights off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        self.logger.info("AudioMusic received new sensor value:" + subject.current_state.name)
        if subject.user == self.user:
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