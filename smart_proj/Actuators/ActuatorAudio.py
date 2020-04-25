import statemachine
import smart_proj.Actuators.Actuator

"""@package docstring
Documentation for this module.

This actuator is the headphones plugged to the audio-guide of 
a visitor

"""


class ActuatorAudio(smart_proj.Actuators.Actuator.Actuator):
    off = statemachine.State('off', initial=True)
    on = statemachine.State('on')

    turn_on = off.to(on)
    turn_off = on.to(off)
