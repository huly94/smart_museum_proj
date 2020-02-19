from smart_proj.Actuators.ActuatorLights import ActuatorLights
from smart_proj.State_machines.LightsManagingMachine import LightsManagingMachine
from smart_proj.Sensors.SensorClock import SensorClock
from smart_proj.Sensors.SensorVisitor import SensorVisitor
from smart_proj.Sensors.SensorWeather import SensorWeather

if __name__ == '__main__':
    mySensor = SensorVisitor()
    mySensorWeather = SensorWeather()
    mySensorClock = SensorClock()
    myState = LightsManagingMachine()

    light = ActuatorLights()

    myState.attach_lights(light)
    mySensor.attach(myState)
    mySensorWeather.attach(myState)
    mySensorClock.attach(myState)

    mySensor.run("visitor_arrived")
    mySensor.run("visitor_left")

    mySensorWeather.run("bad_weather")
    mySensorWeather.run("good_weather")

    mySensorClock.run("day_to_night")
    mySensorClock.run("night_to_day")







