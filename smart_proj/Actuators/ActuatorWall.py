import statemachine
import smart_proj.Actuators.Actuator

"""@package docstring
Documentation for this module.

A smart wall on which visitor can paint using a color they have taken
with a device from a colored light source
"""


class ActuatorWall(smart_proj.Actuators.Actuator.Actuator):
    off = statemachine.State('Off', initial=True)
    on = statemachine.State('On')

    turn_on = off.to(on) | on.to(on)
    turn_off = on.to(off)
