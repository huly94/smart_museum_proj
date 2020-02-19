from smart_proj.Actuators.ActuatorAudio import ActuatorAudio
from smart_proj.Actuators.ActuatorLights import ActuatorLights
from smart_proj.State_machines.AudioVisitorMachine import AudioVisitorMachine
from smart_proj.Sensors.SensorVisitorAge import SensorVisitorAge

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
