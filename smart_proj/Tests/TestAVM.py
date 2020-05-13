import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Apps.AudioVisitorApp
import smart_proj.Actuators.ActuatorAudio
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

    # Step 2.3: Register sensors to orchestrator
    my_orchestrator.register_sensor(my_sensor)

    # Step 2.4: Initialize actuators available in the room
    audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()

    # Step 2.5: Register actuators to orchestrator
    my_orchestrator.register_actuator(audio)

    # In this example there are no other rooms, otherwise,
    # repeat Step 2 for every room available.

    # Step 3.1: Initialize Application
    myApp = smart_proj.Apps.AudioVisitorApp.AudioVisitorMachine()

    # Step 3.2: Register App to orchestrator
    my_orchestrator.register_app(myApp)

    # Step 3.3: Register the Area of the app to the orchestrator
    my_orchestrator.register_area(myApp, "Works area")

    # Step 4: Set the typology of the app
    my_orchestrator.register_typology(myApp, "Individual")

    my_sensor.set_user("1")
    my_sensor.set_area("Works area")

    my_sensor.run("visitor_u18_arrived")
    my_sensor.run("visitor_u18_left")


