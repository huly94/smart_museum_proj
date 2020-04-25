import smart_proj.Sensors.SensorMobile
import smart_proj.Apps.LightGiudeVisitorApp

if __name__ == '__main__':
    # Initialize sensors
    mySensor = smart_proj.Sensors.SensorMobile.SensorMobile()

    # Assign an area to the sensors
    mySensor.set_area("Works area")

    # Assign the user to the sensors
    # Each user has a unique code that can be assigned by reading the tag or in a random way
    # The user is assigned and so the app instantiated when the real sensor detects a new tag
    mySensor.set_user("1")

    mySensor.run('signal_sent')
    mySensor.run('reset')

