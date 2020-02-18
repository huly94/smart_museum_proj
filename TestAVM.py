from ActuatorAudio import ActuatorAudio
from ActuatorLights import ActuatorLights
from AudioVisitorMachine import AudioVisitorMachine
from SensorVisitor import SensorVisitor
from SensorVisitorAge import SensorVisitorAge

if __name__ == '__main__':
    lights1 = ActuatorLights()
    audio = ActuatorAudio()

    mySensor = SensorVisitorAge()

    myState = AudioVisitorMachine()
    #anotherState = AudioVisitorMachine()

    myState.attach_audio(audio)

    mySensor.attach(myState)
    #mySensor.attach(anotherState)

    mySensor.run('visitor_u18_arrived')
    mySensor.run('visitor_u18_left')
