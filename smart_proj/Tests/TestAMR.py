import smart_proj.Apps.AudioMusicRelaxApp
import smart_proj.Sensors.SensorVisitorAge


if __name__ == '__main__':

    # Step 1: Initialize sensors available in the room
    mySensor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    mySensor.set_user("1")
    mySensor.setArea("Relax area")

    mySensor.run('visitor_o18_arrived')
    mySensor.run('visitor_o18_left')
