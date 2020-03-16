import smart_proj.Actuators.ActuatorLights
import smart_proj.Sensors.SensorMobile
import smart_proj.State_machines.LightGiudeVisitorMachine

if __name__ == '__main__':
    myState = smart_proj.State_machines.LightGiudeVisitorMachine.LightGuideVisitorMachine()
    mySensor = smart_proj.Sensors.SensorMobile.SensorMobile()
    light = smart_proj.Actuators.ActuatorLights.ActuatorLights()

    mySensor.attach(myState)
    myState.attach(light)

    mySensor.run('signal_sent')
    mySensor.run('reset')

