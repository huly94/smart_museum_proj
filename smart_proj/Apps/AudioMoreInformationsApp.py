import logging
import statemachine
import smart_proj.Sensors.Sensor
import smart_proj.Apps.Observer


class AudioMoreInformationMachine(smart_proj.Apps.Observer.Observer):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    wait = statemachine.State('Wait', initial=True)
    more_info_provided = statemachine.State('More informations provided')

    play_another_track = wait.to(more_info_provided)
    turn_off = more_info_provided.to(wait)

    visitor = False

    actuator = None

    user = None

    def set_user(self, u):
        self.user = u

    def attach(self, audio):
        self.actuator = audio

    def on_play_another_track(self):
        logging.info("Time out, riproduco un'altra traccia")
        self.actuator.turn_on()

    def on_turn_off(self):
        logging.info("Spento")
        self.actuator.turn_off()
        # when i turn the audio off  i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("AudioMoreInformation received a new sensor value:" + subject.current_state.name)
        if subject.user == self.user and subject.area == "Works area":
            if "Empty" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    self.visitor = False
                    logging.info("no extra audio")
                    # when i turn the audio off  i set the user to -1 in order that the orchestrator remove the app
                    self.set_user("-1")
                elif self.visitor:
                    self.turn_off()
                    self.visitor = False
                else:
                    pass

            elif "Non Empty u18" == subject.current_state.name or "Non Empty o18" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    self.visitor = True
                    logging.info("Waiting for timer...")
                else:
                    pass

            elif "Timer waiting" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    pass
                else:
                    self.turn_off()
                    self.visitor = False

            elif "Timer expired" == subject.current_state.name:
                if "Wait" == self.current_state.name and self.visitor:
                    self.play_another_track()
                else:
                    pass
