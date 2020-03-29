import logging
import statemachine
import smart_proj.Sensors.Sensor
import smart_proj.State_machines.Observer


class AudioMusicRelaxMachine(smart_proj.State_machines.Observer.Observer):
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

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("AudioMusic received new sensor value" + subject.current_state.name)
        if subject.user == self.user:
            if subject.user == self.user:
                if "Empty" == subject.current_state.name:
                    if "Wait" == self.current_state.name:
                        pass
                    else:
                        self.turn_off_music()

                if "Non Empty" == subject.current_state.name:
                    if "Wait" == self.current_state.name:
                        self.play_relaxing_music()
                    else:
                        pass

