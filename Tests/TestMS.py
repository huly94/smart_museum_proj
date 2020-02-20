from smart_proj.Actuators.ActuatorMobile import ActuatorMobile
from smart_proj.Sensors.SensorVisitor import SensorVisitor
from smart_proj.State_machines.MobileSuggestionsMachine import MobileSuggestionsMachine

if __name__ == '__main__':
    myState = MobileSuggestionsMachine()
    mySensor = SensorVisitor()
    mobile = ActuatorMobile()

    mySensor.attach(myState)
    myState.attach_mobile(mobile)

    mySensor.run('visitor_arrived')
    mySensor.run('visitor_left')

