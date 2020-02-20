from statemachine import State

from smart_proj.Sensors.Sensor import Sensor
from smart_proj.State_machines.Observer import Observer


class MobileSuggestionsMachine(Observer):
    wait = State('Wait', initial=True)
    suggestions_received = State('Suggestions received')

    send_suggestions = wait.to(suggestions_received)
    reset = suggestions_received.to(wait)

    actuator = None

    def attach_mobile(self,mobile):
        self.actuator = mobile

    def on_send_suggestions(self):
        print("Suggerimenti inviati")
        self.actuator.turn_on()

    def on_reset(self):
        print("Terminata")
        self.actuator.turn_off()

    def update(self, subject: Sensor):
        print("MobileSuggestion recieved a new sensor value", subject.current_state.name)
        if "Empty" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                pass
            else:
                self.reset()
        if "Non Empty" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                self.send_suggestions()
            else:
                pass
