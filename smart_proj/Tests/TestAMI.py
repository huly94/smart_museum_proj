import smart_proj.Sensors.SensorTimer
import smart_proj.Sensors.SensorVisitorAge

if __name__ == '__main__':
    # Initialize sensors
    mySensorTimer = smart_proj.Sensors.SensorTimer.SensorTimer()
    mySensorVisitor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    # Assign an area to the sensors
    mySensorVisitor.set_area("Works area")
    mySensorTimer.set_area("Works area")

    # Assign the user to the sensors
    # Each user has a unique code that can be assigned by reading the tag or in a random way
    # The user is assigned and so the app instantiated when the real sensor detects a new tag
    mySensorVisitor.set_user("1")
    mySensorTimer.set_user("1")

    # Test phase
    mySensorVisitor.run('visitor_o18_arrived')
    mySensorTimer.run('end_timer')
    mySensorVisitor.run('visitor_o18_left')


    #mySensorTimer.run('reset')

