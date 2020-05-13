import logging
import statemachine
import smart_proj.Sensors.Sensor
import smart_proj.Apps.App

"""@package docstring
Documentation for this module.

At the end of the visit the visitor receive on a device a list of related exhibitions he might like
"""


class MobileSuggestionsMachine(smart_proj.Apps.App.App):
    wait = statemachine.State('Wait', initial=True)
    suggestions_received = statemachine.State('Suggestions received')

    send_suggestions = wait.to(suggestions_received)
    reset = suggestions_received.to(wait)

    actuator = None
    user = None
    
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def set_user(self, u):
        self.user = u

    def dependencies_sensors(self) -> []:
        import smart_proj.Sensors.SensorVisitorAge
        return [smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge]

    def dependencies_actuators(self) -> []:
        import smart_proj.Actuators.ActuatorMobile
        return [smart_proj.Actuators.ActuatorMobile.ActuatorMobile]

    def attach(self, mobile):
        self.actuator = mobile

    def on_send_suggestions(self):
        self.logger.info("Suggerimenti inviati")
        self.actuator.turn_on()

    def on_reset(self):
        self.logger.info("Terminata")
        self.actuator.turn_off()
        # when i turn the mobile off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        self.logger.info("MobileSuggestion recieved a new sensor value:" + subject.current_state.name)
        if "Empty" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                pass
            else:
                self.reset()
        if "Non Empty u18" == subject.current_state.name or "Non Empty o18" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                self.send_suggestions()
            else:
                pass
