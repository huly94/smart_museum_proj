
import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Sensors.SensorVisitor
import smart_proj.State_machines.AudioVisitorMachine
import smart_proj.Sensors.SensorTimer

if __name__ == '__main__':
    #lights1 = smart_proj.Actuators.ActuatorLights.ActuatorLights()
    #audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()

    mySensor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()
    sensor_visitor = smart_proj.Sensors.SensorVisitor.SensorVisitor()
    sensor_timer = smart_proj.Sensors.SensorTimer.SensorTimer()


   # myState = smart_proj.State_machines.AudioVisitorMachine.AudioVisitorMachine()
    #anotherState = AudioVisitorMachine()

    #myState.attach(audio)

    #mySensor.attach(myState)
    #mySensor.attach(anotherState)

    mySensor.run('visitor_u18_arrived')
    sensor_visitor.run("visitor_arrived")
    sensor_timer.run("end_timer")
    #mySensor.run('visitor_u18_left')
