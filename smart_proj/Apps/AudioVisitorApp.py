import logging
import smart_proj.Sensors.Sensor
import smart_proj.Apps.Observer
import statemachine


class AudioVisitorMachine(smart_proj.Apps.Observer.Observer):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    wait = statemachine.State('Wait', initial=True)
    playing_track_u18 = statemachine.State('Playing track for u18')
    playing_track_o18 = statemachine.State('Playing track for o18')

    play_track_u18 = wait.to(playing_track_u18)
    turn_off_track_u18 = playing_track_u18.to(wait)
    play_track_o18 = wait.to(playing_track_o18)
    turn_off_track_o18 = playing_track_o18.to(wait)

    actuator = None
    user = None

    def set_user(self, u):
        self.user = u

    def attach(self, audio):
        self.actuator = audio

    def on_play_track_u18(self):
        logging.info("Playing track for u18")
        self.actuator.turn_on()

    def on_turn_off_track_u18(self):

        logging.info("Turning off")
        self.actuator.turn_off()
        # when i turn the audio off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def on_play_track_o18(self):
        logging.info("Playing track for o18")
        self.actuator.turn_on()

    def on_turn_off_track_o18(self):
        logging.info("Turning off")
        self.actuator.turn_off()
        app = self
        # when i turn the audio off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("AudioVisitor received new sensor value:" + subject.current_state.name)
        if subject.user == self.user:
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
