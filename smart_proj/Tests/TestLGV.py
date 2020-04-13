import smart_proj.Sensors.SensorMobile
import smart_proj.Apps.LightGiudeVisitorApp

if __name__ == '__main__':
    mySensor = smart_proj.Sensors.SensorMobile.SensorMobile()

    mySensor.set_user("1")
    mySensor.setArea("Works area")

    mySensor.run('signal_sent')
    mySensor.run('reset')

