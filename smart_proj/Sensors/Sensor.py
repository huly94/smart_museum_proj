import statemachine
import logging


class Sensor(statemachine.StateMachine):
    logging.basicConfig(format='%(levelname)s:[%(name)s]:%(message)s', level=logging.DEBUG)

    def __init__(self):
        super().__init__()
        self.area = ""
        self.user = ""
        self.position = ""

    # set the area of the sensor
    def set_area(self, r):
        self.area = r

    # set the specific position of the sensor inside the area
    def set_position(self, p):
        self.position = p

    # set the user to which the software instance is dedicated
    def set_user(self, u):
        self.user = u

    # send a value to the orchestrator
    def notify(self):
        import smart_proj.Orchestrator.Orchestrator
        sensor = self
        smart_proj.Orchestrator.Orchestrator.Orchestrator.update(smart_proj.Orchestrator.Orchestrator.Orchestrator.
                                                                 getInstance(), sensor)
