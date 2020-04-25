import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Sensors.SensorTimer
import smart_proj.Sensors.SensorClock
from datetime import datetime


class Room:
    def __init__(self):
        # map where key is a string and value is a string
        # it represents the division in areas of point of interest
        self.point_to_areas = {}
        self.people_at_point = {}
        self.people_in_room = []
        self.point_to_sensor = {}
        self.active_instances_at_point = {}
        self.instances_to_timer = {}
        self.time = 0
        self.night = False

    def add_point_of_interest(self, name, area):
        self.point_to_areas[name] = area
        self.people_at_point[name] = []
        self.active_instances_at_point[name] = []
        self.point_to_sensor[name] = []

    def add_sensor_at_point(self, sensor, point):
        self.point_to_sensor[point].append(sensor)

    def get_available_areas(self):
        return self.point_to_areas.values()

    def get_point_of_interest(self):
        return self.point_to_areas.keys()

    def add_person_in_room(self, visitor):
        self.people_in_room.append(visitor)

    def add_person_at_point(self, visitor, point):
        self.people_at_point[point].append(visitor)

    def add_active_instance(self, sensor, point):
        self.active_instances_at_point[point].append(sensor)

    def update(self):
        self.time += 1/len(self.people_in_room)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time > "17:00:00" and not self.night:
            sensor_clock = smart_proj.Sensors.SensorClock.SensorClock()
            self.night = True
            sensor_clock.run("day_to_night")
        for point in self.point_to_areas.keys():
            i = 0
            while i < len(self.active_instances_at_point[point]):
                sensor = self.active_instances_at_point[point][i]
                user = self.get_visitor_with_tag(sensor.user)
                if user not in self.people_at_point[point]:
                    if user.get_age() > 18:
                        sensor.run("visitor_o18_left")
                    else:
                        sensor.run("visitor_u18_left")
                    self.active_instances_at_point[point].remove(sensor)
                    del self.instances_to_timer[sensor]
                    i -= 1
                i += 1

        for point in self.point_to_areas.keys():
            if len(self.people_at_point[point]) is not 0:
                if "Sensor timer" in self.point_to_sensor[point]:
                    for sensor in self.active_instances_at_point[point]:
                        if sensor.current_state.name == "Non Empty u18" or sensor.current_state.name == "Non Empty o18":
                            self.instances_to_timer[sensor] -= 1
                            if self.instances_to_timer[sensor] == 0:
                                sensor_timer = smart_proj.Sensors.SensorTimer.SensorTimer()
                                sensor_timer.set_user(sensor.user)
                                sensor_timer.set_area(sensor.area)
                                sensor_timer.run("end_timer")

                if "RFID reader" in self.point_to_sensor[point]:
                    for visitor in self.people_at_point[point]:
                        sensor_visitor = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()
                        sensor_visitor.set_user(visitor.tag)
                        sensor_visitor.set_area(self.point_to_areas[point])
                        if not self.exist_instance_at_point(sensor_visitor, point):
                            self.add_active_instance(sensor_visitor, point)
                            self.instances_to_timer[sensor_visitor] = len(self.people_in_room)
                            # case arrived
                            if visitor.get_age() > 18:
                                sensor_visitor.run("visitor_o18_arrived")
                            else:
                                sensor_visitor.run("visitor_u18_arrived")

    def get_visitor_with_tag(self, user):
        for visitor in self.people_in_room:
            if visitor.tag == user:
                return visitor

    def exist_instance_at_point(self, sensor_visitor, point):
        for sensor in self.active_instances_at_point[point]:
            if sensor.user == sensor_visitor.user and sensor.__class__ == sensor_visitor.__class__:
                return True
        return False
