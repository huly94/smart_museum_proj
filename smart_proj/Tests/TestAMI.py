import smart_proj.Actuators.ActuatorAudio
import smart_proj.State_machines.AudioMoreInformationsMachine
import smart_proj.Sensors.SensorTimer
import smart_proj.Sensors.SensorVisitor


if __name__ == '__main__':
    myState = smart_proj.State_machines.AudioMoreInformationsMachine.AudioMoreInformationMachine()
    mySensorTimer = smart_proj.Sensors.SensorTimer.SensorTimer()
    mySensorVisitor = smart_proj.Sensors.SensorVisitor.SensorVisitor()
    audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()

    mySensorTimer.attach(myState)
    mySensorVisitor.attach(myState)

    myState.attach(audio)

    mySensorVisitor.run('visitor_arrived')
    mySensorTimer.run('end_timer')
    mySensorTimer.run('reset')
    mySensorVisitor.run('visitor_left')






