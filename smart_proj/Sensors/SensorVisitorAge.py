import logging

from statemachine import State
from smart_proj.Sensors.Sensor import Sensor


class SensorVisitorAge(Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    empty = State('Empty', initial= True)
    non_empty_u18 = State('Non Empty u18')
    non_empty_o18 = State('Non Empty o18')

    visitor_u18_arrived = empty.to(non_empty_u18)
    visitor_o18_arrived = empty.to(non_empty_o18)
    visitor_o18_left = non_empty_o18.to(empty)
    visitor_u18_left = non_empty_u18.to(empty)

    def __init__(self):
        super().__init__()

    def on_enter_non_empty_u18(self):
        logging.info("[SENSOR VISITOR AGE]: A new visitor u18 has arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_non_empty_o18(self):
        logging.info("[SENSOR VISITOR AGE]: A new visitor o18 has arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_empty(self):
        logging.info("[SENSOR VISITOR AGE]: Visitor has left, new state:" + self.current_state.name)
        self.notify()


