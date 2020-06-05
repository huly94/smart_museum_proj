import smart_proj.Apps.AudioMusicRelaxApp
import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Orchestrator.Orchestrator
import smart_proj.Actuators.ActuatorAudio


if __name__ == '__main__':
    # Step 1: Initialize orchestrator
    my_orchestrator = smart_proj.Orchestrator.Orchestrator.Orchestrator()

    # Step 2.1: Initialize Room
    # Assume that we have only 1 room.
    # In this example, all sensors/actuators refer to the same room.
    # No functionality available yet.

    # Step 2.2: Initialize sensors available in the room
    mySensor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    # Step 2.3: Register sensors to orchestrator
    my_orchestrator.register_sensor(mySensor)

    # Step 2.4: Initialize actuators available in the room
    audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()

    # Step 2.5: Register actuators to orchestrator
    my_orchestrator.register_actuator(audio)

    # In this example there are no other rooms, otherwise,
    # repeat Step 2 for every room available.

    # Step 3.1: Initialize Application
    myApp = smart_proj.Apps.AudioMusicRelaxApp.AudioMusicRelaxMachine()

    # Step 3.1.1: Set the typology of the app
    myApp.set_typology("Individual")

    # Step 3.2: Register App to orchestrator
    my_orchestrator.register_app(myApp)

    # Step 3.3: Register the Area of the app to the orchestrator
    my_orchestrator.register_area(myApp, "Relax area")



    # Assign an area to the sensors
    mySensor.set_area("Relax area")

    # Assign the user to the sensors
    # Each user has a unique code that can be assigned by reading the tag or in a random way
    # The user is assigned and so the app instantiated when the real sensor detects a new tag
    mySensor.set_user("1")

    mySensor.run('visitor_o18_arrived')
    mySensor.run('visitor_o18_left')
