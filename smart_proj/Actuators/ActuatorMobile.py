from statemachine import StateMachine, State


class ActuatorMobile(StateMachine):
    off = State('Off', initial=True)
    on = State('On')

    turn_on = off.to(on)
    turn_off = on.to(off)

    def attach_mobile(self, mobile):
        self.actuator = mobile