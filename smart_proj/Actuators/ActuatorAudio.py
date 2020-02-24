from statemachine import StateMachine, State


class ActuatorAudio(StateMachine):
    off = State('off', initial=True)
    on = State('on')

    turn_on = off.to(on)
    turn_off = on.to(off)

    def attach_audio(self, audio):
        self.actuator = audio