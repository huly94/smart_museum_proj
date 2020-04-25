import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Apps.InteractiveWorkApp

if __name__ == '__main__':
    # Initialize sensors
    mySensor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    # Assign an area to the sensors
    mySensor.set_area("Interactive work area")

    # Assign the user to the sensors
    # Each user has a unique code that can be assigned by reading the tag or in a random way
    # The user is assigned and so the app instantiated when the real sensor detects a new tag
    mySensor.set_user("1")

    mySensor.run('visitor_u18_arrived')
    mySensor.run('visitor_u18_left')
