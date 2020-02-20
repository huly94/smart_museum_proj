from smart_proj.Actuators.ActuatorLights import ActuatorLights
from smart_proj.Sensors.SensorMobile import SensorMobile
from smart_proj.State_machines.LightGiudeVisitorMachine import LightGuideVisitorMachine

if __name__ == '__main__':
    myState = LightGuideVisitorMachine()
    mySensor = SensorMobile()
    light = ActuatorLights()

    mySensor.attach(myState)
    myState.attach_lights(light)

    mySensor.run('signal_sent')
    mySensor.run('reset')

