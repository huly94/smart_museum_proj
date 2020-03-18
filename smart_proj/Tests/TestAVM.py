
import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Sensors.SensorVisitor
import smart_proj.Sensors.SensorTimer
import smart_proj.Sensors.SensorWeather
import smart_proj.Sensors.SensorColors
import smart_proj.Sensors.SensorGesture
import smart_proj.Sensors.SensorClock
import smart_proj.Sensors.SensorMobile

if __name__ == '__main__':
    #lights1 = smart_proj.Actuators.ActuatorLights.ActuatorLights()
    #audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()

    mySensor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()
    sensor_visitor = smart_proj.Sensors.SensorVisitor.SensorVisitor()
    sensor_timer = smart_proj.Sensors.SensorTimer.SensorTimer()
    sensor_color = smart_proj.Sensors.SensorColors.SensorColors()
    sensor_gesture = smart_proj.Sensors.SensorGesture.SensorGesture()
    mySensorWeather = smart_proj.Sensors.SensorWeather.SensorWeather()
    mySensorClock = smart_proj.Sensors.SensorClock.SensorClock()
    mySensorMobile = smart_proj.Sensors.SensorMobile.SensorMobile()

    #mySensorMobile.run('signal_sent')
    #mySensorMobile.run('reset')

    sensor_visitor.setArea("relax area")


    #mySensor.run('visitor_u18_arrived')

    sensor_visitor.run("visitor_arrived")
    sensor_visitor.run("visitor_left")

    #sensor_timer.run("end_timer")

    #sensor_color.run("blue_detected")
    #sensor_gesture.run("gesture_detected")

    #mySensorClock.run("day_to_night")
    #mySensorClock.run("night_to_day")

    #mySensorWeather.run("bad_weather")
    #mySensorWeather.run("good_weather")
    #mySensor.run('visitor_u18_left')
