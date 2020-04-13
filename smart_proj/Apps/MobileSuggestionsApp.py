import logging
import statemachine
import smart_proj.Sensors.Sensor
import smart_proj.Apps.Observer


class MobileSuggestionsMachine(smart_proj.Apps.Observer.Observer):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    wait = statemachine.State('Wait', initial=True)
    suggestions_received = statemachine.State('Suggestions received')

    send_suggestions = wait.to(suggestions_received)
    reset = suggestions_received.to(wait)

    actuator = None
    user = None

    def set_user(self, u):
        self.user = u

    def attach(self, mobile):
        self.actuator = mobile

    def on_send_suggestions(self):
        logging.info("Suggerimenti inviati")
        self.actuator.turn_on()

    def on_reset(self):
        logging.info("Terminata")
        self.actuator.turn_off()
        import smart_proj.Orchestrator.Orchestrator
        # when i turn the mobile off i remove the app from the orchestrator
        app = self
        smart_proj.Orchestrator.Orchestrator.Orchestrator. \
            remove_app(smart_proj.Orchestrator.Orchestrator.Orchestrator.getInstance(), app)

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("MobileSuggestion recieved a new sensor value:" + subject.current_state.name)
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
