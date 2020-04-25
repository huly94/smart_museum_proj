import logging
import statemachine
import smart_proj.Sensors.Sensor


# A RFID sensor reader
# once that the physical reader detect an audio player, it uses the information that receives to create an instance of
# this sensor dedicated to the user
class SensorVisitorAge(smart_proj.Sensors.Sensor.Sensor):
    empty = statemachine.State('Empty', initial=True)
    non_empty_u18 = statemachine.State('Non Empty u18')
    non_empty_o18 = statemachine.State('Non Empty o18')

    visitor_u18_arrived = empty.to(non_empty_u18) | non_empty_u18.to(non_empty_u18) | non_empty_o18.to(non_empty_u18)
    visitor_o18_arrived = empty.to(non_empty_o18) | non_empty_o18.to(non_empty_o18) | non_empty_u18.to(non_empty_o18)
    visitor_o18_left = non_empty_o18.to(empty)
    visitor_u18_left = non_empty_u18.to(empty)

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def on_enter_non_empty_u18(self):
        self.logger.info("A new visitor u18 has arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_non_empty_o18(self):
        self.logger.info("A new visitor o18 has arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_empty(self):
        self.logger.info("Visitor has left, new state:" + self.current_state.name)
        self.notify()
