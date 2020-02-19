from statemachine import StateMachine, State


class ActuatorLights(StateMachine):
    off = State('off', initial=True)
    on = State('on')
    turn_on = off.to(on)
    turn_off = on.to(off)

    def attach_lights(self, lights):
        self.actuator = lights



