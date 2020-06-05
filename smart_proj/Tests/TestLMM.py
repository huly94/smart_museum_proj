import smart_proj.Sensors.SensorClock
import smart_proj.Sensors.SensorWeather
import smart_proj.Sensors.SensorPresence
import smart_proj.Actuators.ActuatorLights
import smart_proj.Apps.LightsManagingApp
import smart_proj.Orchestrator.Orchestrator

if __name__ == '__main__':
    # Step 1: Initialize orchestrator
    my_orchestrator = smart_proj.Orchestrator.Orchestrator.Orchestrator()

    # Step 2.1: Initialize Room
    # Assume that we have only 1 room.
    # In this example, all sensors/actuators refer to the same room.
    # No functionality available yet.

    # Step 2.2: Initialize sensors available in the room
    mySensor = smart_proj.Sensors.SensorPresence.SensorPresence()
    mySensorClock = smart_proj.Sensors.SensorClock.SensorClock()
    mySensorWeather = smart_proj.Sensors.SensorWeather.SensorWeather()

    # Step 2.3: Register sensors to orchestrator
    my_orchestrator.register_sensor(mySensor)
    my_orchestrator.register_sensor(mySensorClock)
    my_orchestrator.register_sensor(mySensorWeather)

    # Step 2.4: Initialize actuators available in the room
    lights = smart_proj.Actuators.ActuatorLights.ActuatorLights()

    # Step 2.5: Register actuators to orchestrator
    my_orchestrator.register_actuator(lights)

    # In this example there are no other rooms, otherwise,
    # repeat Step 2 for every room available.

    # Step 3.1: Initialize Application
    myApp = smart_proj.Apps.LightsManagingApp.LightsManagingMachine()

    # Step 3.1.1: Set the typology of the app
    myApp.set_typology("General")

    # Step 3.2: Register App to orchestrator
    my_orchestrator.register_app(myApp)

    # In this example there is only 1 app, otherwise,
    # repeat Step 3 for every app needed.

    # Try out different scenarios by playing with the sensors
    print("Case 1: ON/OFF")
    mySensor.run("visitor_arrived")
    mySensor.run("visitor_left")

    print("Case 2: ON/OFF")
    mySensorWeather.run("bad_weather")
    mySensorWeather.run("good_weather")

    print("Case 3: ON/OFF")
    mySensorClock.run("day_to_night")
    mySensorClock.run("night_to_day")

    print("Case 4: Always ON")
    mySensor.run("visitor_arrived")
    mySensorClock.run("day_to_night")
    mySensor.run("visitor_left")
    mySensorWeather.run("bad_weather")
