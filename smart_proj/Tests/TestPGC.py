import logging

import smart_proj.Actuators.ActuatorMobile
import smart_proj.Actuators.ActuatorWall
import smart_proj.Sensors.SensorColors
import smart_proj.Sensors.SensorGesture
import smart_proj.Apps.PervasiveGameChromatizeIt

if __name__ == '__main__':
    myState = smart_proj.Apps.PervasiveGameChromatizeIt.PervasiveGameChromatizeIt()
    mySensor = smart_proj.Sensors.SensorColors.SensorColors()
    mySensorGesture = smart_proj.Sensors.SensorGesture.SensorGesture()
    mobile = smart_proj.Actuators.ActuatorMobile.ActuatorMobile()
    wall = smart_proj.Actuators.ActuatorWall.ActuatorWall()

    mySensor.attach(myState)
    mySensorGesture.attach(myState)
    myState.attach_mobile(mobile)
    myState.attach_wall(wall)

    mySensor.run("blue_detected")
    mySensorGesture.run("gesture_detected")
    mySensorGesture.run("gesture_detected")
    mySensorGesture.run("no_gesture")



