import smart_proj.Actuators.ActuatorMobile
import smart_proj.Sensors.SensorVisitor
import smart_proj.Apps.MobileSuggestionsApp


if __name__ == '__main__':

    myState = smart_proj.Apps.MobileSuggestionsApp.MobileSuggestionsMachine()
    mySensor = smart_proj.Sensors.SensorVisitor.SensorVisitor()
    mobile = smart_proj.Actuators.ActuatorMobile.ActuatorMobile()

    mySensor.attach(myState)
    myState.attach(mobile)

    mySensor.run('visitor_arrived')
    mySensor.run('visitor_left')
