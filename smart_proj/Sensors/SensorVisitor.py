import logging
import statemachine
import smart_proj.Sensors.Sensor


class SensorVisitor(smart_proj.Sensors.Sensor.Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    empty = statemachine.State('Empty', initial=True)
    non_empty = statemachine.State('Non Empty')

    visitor_arrived = empty.to(non_empty)
    visitor_left = non_empty.to(empty)

    def __init__(self):
        super().__init__()

    def on_enter_non_empty(self):
        logging.info("[SENSOR VISITOR]: A new visitor has arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_empty(self):
        logging.info("[SENSOR VISITOR]: Visitor has left, new state:" + self.current_state.name)
        self.notify()
