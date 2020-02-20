from statemachine import StateMachine, State


class ActuatorPainting(StateMachine):
    off = State('Off', initial=True)
    on = State('On')

    turn_on = off.to(on)
    turn_off = on.to(off)

    def attach_painting(self, painting):
        self.actuator = painting