import logging
import statemachine
import smart_proj.Sensors.Sensor
import smart_proj.Apps.Observer


class AudioMusicRelaxMachine(smart_proj.Apps.Observer.Observer):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    wait = statemachine.State('Wait', initial=True)
    sound_on = statemachine.State('Sound on')

    play_relaxing_music = wait.to(sound_on)
    turn_off_music = sound_on.to(wait)

    actuator = None

    user = None

    def set_user(self, u):
        self.user = u

    def attach(self, audio):
        self.actuator = audio

    def on_play_relaxing_music(self):
        logging.info("riproduco musica rilassante")
        self.actuator.turn_on()

    def on_turn_off_music(self):
        logging.info("Spengo musica")
        self.actuator.turn_off()
        # when i turn the audio off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("AudioMusic received new sensor value" + subject.current_state.name)
        if subject.user == self.user and subject.area == "Relax area":
            if subject.user == self.user:
                if "Empty" == subject.current_state.name:
                    if "Wait" == self.current_state.name:
                        pass
                    else:
                        self.turn_off_music()

                if "Non Empty u18" == subject.current_state.name or "Non Empty o18" == subject.current_state.name:  # if someone arrives
                    if "Wait" == self.current_state.name:
                        self.play_relaxing_music()
                    else:
                        pass

