import smart_proj.Sensors.SensorTimer
import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Actuators.ActuatorAudio
import smart_proj.Apps.AudioVisitorApp
import smart_proj.Apps.AudioMoreInformationsApp
import smart_proj.Orchestrator.Orchestrator

if __name__ == '__main__':
    # Step 1: Initialize orchestrator
    my_orchestrator = smart_proj.Orchestrator.Orchestrator.Orchestrator()

    # Step 2.1: Initialize Room
    # Assume that we have only 1 room.
    # In this example, all sensors/actuators refer to the same room.
    # No functionality available yet.

    # Step 2.2: Initialize sensors available in the room
    my_sensor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()
    mySensorTimer = smart_proj.Sensors.SensorTimer.SensorTimer()

    # Step 2.3: Register sensors to orchestrator
    my_orchestrator.register_sensor(my_sensor)
    my_orchestrator.register_sensor(mySensorTimer)

    # Step 2.4: Initialize actuators available in the room
    audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()

    # Step 2.5: Register actuators to orchestrator
    my_orchestrator.register_actuator(audio)

    # In this example there are no other rooms, otherwise,
    # repeat Step 2 for every room available.

    # Step 3.1: Initialize Application
    myApp = smart_proj.Apps.AudioVisitorApp.AudioVisitorMachine()
    myAppMoreInfo = smart_proj.Apps.AudioMoreInformationsApp.AudioMoreInformationMachine()

    # Step 3.1.1: Set the typology of the app
    myApp.set_typology("Individual")
    myAppMoreInfo.set_typology("Individual")

    # Step 3.2: Register App to orchestrator
    my_orchestrator.register_app(myApp)
    my_orchestrator.register_app(myAppMoreInfo)

    # Step 3.3: Register the Area of the app to the orchestrator
    my_orchestrator.register_area(myApp, "Works area")
    my_orchestrator.register_area(myAppMoreInfo, "Works area")

    # Assign an area to the sensors
    my_sensor.set_area("Works area")
    mySensorTimer.set_area("Works area")

    # Assign the user to the sensors
    # Each user has a unique code that can be assigned by reading the tag or in a random way
    # The user is assigned and so the app instantiated when the real sensor detects a new tag
    my_sensor.set_user("1")
    mySensorTimer.set_user("1")

    # Test phase
    my_sensor.run('visitor_o18_arrived')
    mySensorTimer.run('end_timer')
    my_sensor.run('visitor_o18_left')

    # mySensorTimer.run('reset')
