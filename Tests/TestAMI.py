from smart_proj.Actuators.ActuatorAudio import ActuatorAudio
from smart_proj.State_machines.AudioMoreInformationsMachine import AudioMoreInformationMachine
from smart_proj.Sensors.SensorTimer import SensorTimer
from smart_proj.Sensors.SensorVisitor import SensorVisitor


if __name__ == '__main__':
    myState = AudioMoreInformationMachine()
    mySensorTimer = SensorTimer()
    mySensorVisitor = SensorVisitor()
    audio = ActuatorAudio()

    mySensorTimer.attach(myState)
    mySensorVisitor.attach(myState)

    myState.attach_audio(audio)

    mySensorVisitor.run('visitor_arrived')
    mySensorTimer.run('end_timer')
    mySensorTimer.run('reset')
    mySensorVisitor.run('visitor_left')






