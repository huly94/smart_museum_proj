import statemachine
import smart_proj.Actuators.Actuator

"""@package docstring
Documentation for this module.

A painting can be animated in the case of an 
interactive work
"""


class ActuatorPainting(smart_proj.Actuators.Actuator.Actuator):
    off = statemachine.State('Off', initial=True)
    on = statemachine.State('On')

    turn_on = off.to(on)
    turn_off = on.to(off)
