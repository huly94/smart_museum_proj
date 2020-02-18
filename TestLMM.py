from ActuatorAudio import ActuatorAudio
from ActuatorLights import ActuatorLights
from AudioVisitorMachine import AudioVisitorMachine
from LightsManagingMachine import LightsManagingMachine
from SensorClock import SensorClock
from SensorVisitor import SensorVisitor
from SensorVisitorAge import SensorVisitorAge
from SensorWeather import SensorWeather

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







