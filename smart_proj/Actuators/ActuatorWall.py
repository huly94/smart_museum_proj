from statemachine import StateMachine, State


class ActuatorWall(StateMachine):
    off = State('Off', initial=True)
    on = State('On')

    turn_on = off.to(on) | on.to(on)
    turn_off = on.to(off)

    def attach_wall(self, wall):
        self.actuator = wall