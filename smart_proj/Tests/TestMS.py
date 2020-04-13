import smart_proj.Sensors.SensorVisitorAge


if __name__ == '__main__':

    mySensor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()

    mySensor.setArea("Exit area")
    mySensor.set_user("1")

    mySensor.run('visitor_u18_arrived')
    mySensor.run('visitor_u18_left')
