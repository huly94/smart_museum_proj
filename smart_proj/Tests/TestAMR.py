import smart_proj.Actuators.ActuatorAudio
import smart_proj.Apps.AudioMusicRelaxApp
import smart_proj.Sensors.SensorVisitor


if __name__ == '__main__':
    myState = smart_proj.Apps.AudioMusicRelaxApp.AudioMusicRelaxMachine()
    mySensor = smart_proj.Sensors.SensorVisitor.SensorVisitor()
    audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()

    mySensor.attach(myState)
    myState.attach(audio)

    mySensor.run('visitor_arrived')
    mySensor.run('visitor_left')
