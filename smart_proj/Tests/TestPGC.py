import smart_proj.Sensors.SensorColors
import smart_proj.Sensors.SensorGesture
import smart_proj.Apps.PervasiveGameChromatizeIt

if __name__ == '__main__':
    mySensor = smart_proj.Sensors.SensorColors.SensorColors()
    mySensorGesture = smart_proj.Sensors.SensorGesture.SensorGesture()

    mySensor1 = smart_proj.Sensors.SensorColors.SensorColors()
    mySensorGesture1 = smart_proj.Sensors.SensorGesture.SensorGesture()

    mySensor.set_user("1")
    mySensorGesture.set_user("1")

    mySensor.set_user("2")
    mySensorGesture.set_user("2")

    mySensor.set_area("Game area")
    mySensorGesture.set_area("Game area")

    mySensor1.set_area("Game area")
    mySensorGesture1.set_area("Game area")

    mySensor.run("blue_detected")
    mySensor1.run("red_detected")
    mySensorGesture.run("gesture_detected")
    mySensorGesture.run("no_gesture")
