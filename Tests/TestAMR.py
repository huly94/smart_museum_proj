from smart_proj.Actuators.ActuatorAudio import ActuatorAudio
from smart_proj.Sensors.SensorVisitor import SensorVisitor
from smart_proj.State_machines.AudioMusicRelaxMachine import AudioMusicRelaxMachine

if __name__ == '__main__':
    myState = AudioMusicRelaxMachine()
    mySensor = SensorVisitor()
    audio = ActuatorAudio()

    mySensor.attach(myState)
    myState.attach_sound(audio)

    mySensor.run('visitor_arrived')
    mySensor.run('visitor_left')


