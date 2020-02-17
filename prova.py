from ActuatorLights import ActuatorLights
from AudioVisitorMachine import AudioVisitorMachine
from SensorVisitor import SensorVisitor

if __name__ == '__main__':
    lights1 = ActuatorLights()

    mySensor = SensorVisitor()

    myState = AudioVisitorMachine()
    anotherState = AudioVisitorMachine()

    myState.attach_lights(lights1)

    mySensor.attach(myState)
    mySensor.attach(anotherState)

    mySensor.run('visitor_arrived')
