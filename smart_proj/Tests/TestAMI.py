import smart_proj.Sensors.SensorTimer
import smart_proj.Sensors.SensorVisitorAge

if __name__ == '__main__':
    mySensorTimer = smart_proj.Sensors.SensorTimer.SensorTimer()
    mySensorVisitor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    mySensorVisitor.set_user("1")
    mySensorVisitor.setArea("Works area")

    mySensorTimer.setArea("Works area")
    mySensorTimer.set_user("1")

    mySensorVisitor.run('visitor_o18_arrived')
    mySensorTimer.run('end_timer')
    mySensorVisitor.run('visitor_o18_left')
    mySensorTimer.run('reset')

