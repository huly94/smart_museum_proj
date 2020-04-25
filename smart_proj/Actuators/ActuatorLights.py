import statemachine
import smart_proj.Actuators.Actuator

"""@package docstring
Documentation for this module.

The lights that are turned on or off by the lights managing app
also they they can be turned on with a different color to show the path to a visitor

"""


class ActuatorLights(smart_proj.Actuators.Actuator.Actuator):
    off = statemachine.State('off', initial=True)
    on = statemachine.State('on')
    turn_on = off.to(on)
    turn_off = on.to(off)
