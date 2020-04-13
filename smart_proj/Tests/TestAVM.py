import smart_proj.Sensors.SensorVisitorAge

if __name__ == '__main__':

    sva1 = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    sva2 = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    sva1.set_user("1")
    sva1.setArea("Works area")

    sva2.set_user("2")
    sva2.setArea("Works area")

    sva1.run("visitor_u18_arrived")
    sva2.run("visitor_o18_arrived")
    sva1.run("visitor_u18_left")
    sva2.run("visitor_o18_left")
