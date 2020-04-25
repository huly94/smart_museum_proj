import logging

import statemachine

import smart_proj.Sensors.Sensor


# A simple Occupancy Sensor (probably a Passive InfraRed sensor)
# that detects if there is at least 1 visitor in the area or none.
# It cannot differentiate between different visitors and cannot count how many visitors are in the room.
#
# We assume that the sensor internally includes a timer.
# If no motion event is received after a given period of time, the sensor assumes that
# the room is no longer occupied by a visitor.
# When the sensor receives consecutive motion detection events, it will suppress them.
class SensorPresence(smart_proj.Sensors.Sensor.Sensor):

    empty = statemachine.State("Not detected", initial= True)
    non_empty = statemachine.State("Person detected")

    visitor_arrived = empty.to(non_empty)
    visitor_left = non_empty.to(empty)

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def on_enter_non_empty(self):
        self.logger.info("A new visitor has arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_empty(self):
        self.logger.info("Visitor has left, new state:" + self.current_state.name)
        self.notify()
