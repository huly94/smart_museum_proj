import smart_proj.Actuators.ActuatorLights
import smart_proj.Sensors.SensorMobile
import smart_proj.Apps.LightGiudeVisitorApp

if __name__ == '__main__':
    myState = smart_proj.Apps.LightGiudeVisitorApp.LightGuideVisitorMachine()
    mySensor = smart_proj.Sensors.SensorMobile.SensorMobile()
    light = smart_proj.Actuators.ActuatorLights.ActuatorLights()

    mySensor.attach(myState)
    myState.attach(light)

    mySensor.run('signal_sent')
    mySensor.run('reset')

