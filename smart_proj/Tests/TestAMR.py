import smart_proj.Apps.AudioMusicRelaxApp
import smart_proj.Sensors.SensorVisitorAge


if __name__ == '__main__':

    # Step 1: Initialize sensors available in the room
    mySensor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    # Assign an area to the sensors
    mySensor.set_area("Relax area")

    # Assign the user to the sensors
    # Each user has a unique code that can be assigned by reading the tag or in a random way
    # The user is assigned and so the app instantiated when the real sensor detects a new tag
    mySensor.set_user("1")

    mySensor.run('visitor_o18_arrived')
    mySensor.run('visitor_o18_left')
