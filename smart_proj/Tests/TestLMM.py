import smart_proj.Actuators.ActuatorLights
import smart_proj.State_machines.LightsManagingApp
import smart_proj.Sensors.SensorClock
import smart_proj.Sensors.SensorVisitor
import smart_proj.Sensors.SensorWeather

if __name__ == '__main__':
    mySensor = smart_proj.Sensors.SensorVisitor.SensorVisitor()
    mySensorWeather = smart_proj.Sensors.SensorWeather.SensorWeather()
    mySensorClock = smart_proj.Sensors.SensorClock.SensorClock()
    myState = smart_proj.State_machines.LightsManagingApp.LightsManagingMachine()

    light = smart_proj.Actuators.ActuatorLights.ActuatorLights()

    myState.attach(light)
    mySensor.attach(myState)
    mySensorWeather.attach(myState)
    mySensorClock.attach(myState)

    mySensor.run("visitor_arrived")
    mySensor.run("visitor_left")

    mySensorWeather.run("bad_weather")
    mySensorWeather.run("good_weather")

    mySensorClock.run("day_to_night")
    mySensorClock.run("night_to_day")








