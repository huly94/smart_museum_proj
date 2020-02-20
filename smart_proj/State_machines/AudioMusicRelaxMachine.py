from statemachine import State

from smart_proj.Sensors.Sensor import Sensor
from smart_proj.State_machines.Observer import Observer


class AudioMusicRelaxMachine(Observer):
    wait = State('Wait', initial=True)
    sound_on = State('Sound on')

    play_relaxing_music = wait.to(sound_on)
    turn_off_music = sound_on.to(wait)

    actuator = None

    def attach_sound(self, audio):
        self.actuator = audio

    def on_play_relaxing_music(self):
        print("riproduco musica rilassante")
        self.actuator.turn_on()

    def on_turn_off_music(self):
        print("Spengo musica")
        self.actuator.turn_off()

    def update(self, subject: Sensor):
        print("AudioMusic received new sensor value", subject.current_state.name)
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

