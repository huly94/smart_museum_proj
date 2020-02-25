import logging

from smart_proj.Actuators.ActuatorMobile import ActuatorMobile
from smart_proj.Actuators.ActuatorWall import ActuatorWall
from smart_proj.Sensors.SensorColors import SensorColors
from smart_proj.Sensors.SensorGesture import SensorGesture
from smart_proj.State_machines.PervasiveGameChromatizeIt import PervasiveGameChromatizeIt

if __name__ == '__main__':
    myState = PervasiveGameChromatizeIt()
    mySensor = SensorColors()
    mySensorGesture = SensorGesture()
    mobile = ActuatorMobile()
    wall = ActuatorWall()

    mySensor.attach(myState)
    mySensorGesture.attach(myState)
    myState.attach_mobile(mobile)
    myState.attach_wall(wall)

    mySensor.run("blue_detected")
    mySensorGesture.run("gesture_detected")
    mySensorGesture.run("gesture_detected")
    mySensorGesture.run("no_gesture")



