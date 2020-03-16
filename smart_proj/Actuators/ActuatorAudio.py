import statemachine
import smart_proj.Actuators.Actuator


class ActuatorAudio(smart_proj.Actuators.Actuator.Actuator):
    off = statemachine.State('off', initial=True)
    on = statemachine.State('on')

    turn_on = off.to(on)
    turn_off = on.to(off)

