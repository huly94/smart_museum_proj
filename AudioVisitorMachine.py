from Observer import Observer
from Sensor import Sensor
from statemachine import StateMachine, State


class AudioVisitorMachine(Observer):
    wait = State('Wait', initial=True)
    playing_track_u18 = State('Playing track for u18')
    playing_track_o18 = State('Playing track for o18')

    play_track_u18 = wait.to(playing_track_u18)
    turn_off_track_u18 = playing_track_u18.to(wait)
    play_track_o18 = wait.to(playing_track_o18)
    turn_off_track_o18 = playing_track_o18.to(wait)

    actuator = None

    def attach_audio(self, audio):
        self.actuator = audio

    def on_play_track_u18(self):
        print("Acceso")
        self.actuator.turn_on()

    def on_turn_off_track_u18(self):
        print("Spento")
        self.actuator.turn_off()

    def on_play_track_o18(self):
        print("Acceso")
        self.actuator.turn_on()

    def on_turn_off_track_o18(self):
        print("Spento")
        self.actuator.turn_off()

    def update(self, subject: Sensor):
        print("AudioVisitor received new sensor value", subject.current_state.name)
        if "Empty" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                pass
            else:
                try:
                    self.turn_off_track_o18()
                except:
                    self.turn_off_track_u18()

        elif "Non Empty u18" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                self.play_track_u18()
            else:
                pass

        elif "Non Empty o18" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                self.play_track_o18()
            else:
                pass


