import smart_proj.Actuators.ActuatorPainting
import smart_proj.Sensors.SensorVisitor
import smart_proj.State_machines.InteractiveWorkMachine

if __name__ == '__main__':
    myState = smart_proj.State_machines.InteractiveWorkMachine.InteractiveWorkMachine()
    mySensor = smart_proj.Sensors.SensorVisitor.SensorVisitor()
    painting = smart_proj.Actuators.ActuatorPainting.ActuatorPainting()

    mySensor.attach(myState)
    myState.attach(painting)

    mySensor.run('visitor_arrived')
    mySensor.run('visitor_left')




