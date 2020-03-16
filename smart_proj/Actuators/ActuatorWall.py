import statemachine
import smart_proj.Actuators.Actuator


class ActuatorWall(smart_proj.Actuators.Actuator.Actuator):
    off = statemachine.State('Off', initial=True)
    on = statemachine.State('On')

    turn_on = off.to(on) | on.to(on)
    turn_off = on.to(off)

