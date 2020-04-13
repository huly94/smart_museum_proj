import smart_proj.Sensors.SensorClock
import smart_proj.Sensors.SensorWeather
import smart_proj.Sensors.SensorPresence

if __name__ == '__main__':


    # Step 2.1: Initialize Room
    # Assume that we have only 1 room.
    # In this example, all sensors/actuators refer to the same room.
    # No functionality available yet.

    # Step 2.2: Initialize sensors available in the room
    mySensorPir = smart_proj.Sensors.SensorPresence.SensorPresence()
    mySensorWeather = smart_proj.Sensors.SensorWeather.SensorWeather()
    mySensorClock = smart_proj.Sensors.SensorClock.SensorClock()

    mySensorClock.run("day_to_night")
    # Try out different scenarios by playing with the sensors
    mySensorPir.run("visitor_arrived")
    mySensorPir.run("visitor_left")

    #Case 4: Always ON
    mySensorPir.run("visitor_arrived")
    mySensorPir.run("visitor_left")
    mySensorWeather.run("bad_weather")
