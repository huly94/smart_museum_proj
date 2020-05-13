import smart_proj.Sensors.SensorColors
import smart_proj.Sensors.SensorGesture
import smart_proj.Apps.PervasiveGameChromatizeIt
import smart_proj.Actuators.ActuatorMobile
import smart_proj.Actuators.ActuatorWall
import smart_proj.Orchestrator.Orchestrator

if __name__ == '__main__':
    # Step 1: Initialize orchestrator
    my_orchestrator = smart_proj.Orchestrator.Orchestrator.Orchestrator()

    # Step 2.1: Initialize Room
    # Assume that we have only 1 room.
    # In this example, all sensors/actuators refer to the same room.
    # No functionality available yet.

    # Step 2.2: Initialize sensors available in the room
    mySensor = smart_proj.Sensors.SensorColors.SensorColors()
    mySensorGesture = smart_proj.Sensors.SensorGesture.SensorGesture()

    # Step 2.3: Register sensors to orchestrator
    my_orchestrator.register_sensor(mySensor)
    my_orchestrator.register_sensor(mySensorGesture)

    # Step 2.4: Initialize actuators available in the room
    mobile = smart_proj.Actuators.ActuatorMobile.ActuatorMobile()
    wall = smart_proj.Actuators.ActuatorWall.ActuatorWall()

    # Step 2.5: Register actuators to orchestrator
    my_orchestrator.register_actuator(mobile)
    my_orchestrator.register_actuator(wall)

    # In this example there are no other rooms, otherwise,
    # repeat Step 2 for every room available.

    # Step 3.1: Initialize Application
    myApp = smart_proj.Apps.PervasiveGameChromatizeIt.PervasiveGameChromatizeIt()

    # Step 3.2: Register App to orchestrator
    my_orchestrator.register_app(myApp)

    # Step 3.3: Register the Area of the app to the orchestrator
    my_orchestrator.register_area(myApp, "Game area")

    # Step 4: Set the typology of the app
    my_orchestrator.register_typology(myApp, "Individual")

    mySensor.set_user("1")
    mySensorGesture.set_user("1")

    mySensor.set_area("Game area")
    mySensorGesture.set_area("Game area")

    mySensor.run("blue_detected")
    mySensorGesture.run("gesture_detected")
    mySensorGesture.run("no_gesture")
