import logging

import statemachine

import smart_proj.Sensors.Sensor
import smart_proj.State_machines.Observer


class LightGuideVisitorMachine(smart_proj.State_machines.Observer.Observer):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    colored_light_off_on_a_related_painting = statemachine.State('Colored light off', initial=True)
    colored_light_on_on_a_related_painting = statemachine.State('Colored light on')

    switch_on_colored_light = colored_light_off_on_a_related_painting.to(colored_light_on_on_a_related_painting)
    switch_off_light = colored_light_on_on_a_related_painting.to(colored_light_off_on_a_related_painting)

    actuator = None

    user = None

    def set_user(self, u):
        self.user = u

    def attach(self, light):
        self.actuator = light

    def on_switch_on_colored_light(self):
        logging.info("Accendi luce colorata su un altro dipinto")
        self.actuator.turn_on()

    def on_switch_off_light(self):
        logging.info("Switch off light")
        self.actuator.turn_off()
        import smart_proj.Orchestrator.Orchestrator
        app = self
        smart_proj.Orchestrator.Orchestrator.Orchestrator. \
            remove_app(smart_proj.Orchestrator.Orchestrator.Orchestrator.getInstance(), app)

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("AudioMusic received new sensor value:" + subject.current_state.name)
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