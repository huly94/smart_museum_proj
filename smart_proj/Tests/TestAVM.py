import smart_proj.Sensors.SensorVisitorAge

if __name__ == '__main__':

    # Step 1: Initialize sensors available in the room
    sva1 = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()
    sva2 = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    # Assign an area to the sensors
    sva1.set_area("Works area")
    sva2.set_area("Works area")

    # Assign the user to the sensors
    # Each user has a unique code that can be assigned by reading the tag or in a random way
    # The user is assigned and so the app instantiated when the real sensor detects a new tag
    sva1.set_user("1")
    sva2.set_user("2")

    sva1.run("visitor_u18_arrived")
    sva2.run("visitor_o18_arrived")
    sva1.run("visitor_u18_left")
    sva2.run("visitor_o18_left")
