import statemachine

import smart_proj.Actuators.Actuator

"""@package docstring
Documentation for this module.

In this case the actuator can be a mobile or any device to which 
we can send message like suggestions on related exhibitions or works


"""


class ActuatorMobile(smart_proj.Actuators.Actuator.Actuator):
    off = statemachine.State('Off', initial=True)
    on = statemachine.State('On')

    turn_on = off.to(on) | on.to(on)
    turn_off = on.to(off)
