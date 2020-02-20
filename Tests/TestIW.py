from smart_proj.Actuators.ActuatorPainting import ActuatorPainting
from smart_proj.Sensors.SensorVisitor import SensorVisitor
from smart_proj.State_machines.InteractiveWorkMachine import InteractiveWorkMachine

if __name__ == '__main__':
    myState = InteractiveWorkMachine()
    mySensor = SensorVisitor()
    painting = ActuatorPainting()

    mySensor.attach(myState)
    myState.attach_painting(painting)

    mySensor.run('visitor_arrived')
    mySensor.run('visitor_left')




