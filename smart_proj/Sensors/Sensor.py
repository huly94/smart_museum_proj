import statemachine
import logging


class Sensor(statemachine.StateMachine):
    logging.basicConfig(format='%(levelname)s:[%(name)s]:%(message)s', level=logging.DEBUG)

    def __init__(self):
        super().__init__()
        self.area = ""
        self.user = ""

    def set_area(self, r):
        self.area = r

    def set_user(self, u):
        self.user = u

    def notify(self):
        import smart_proj.Orchestrator.Orchestrator
        sensor = self
        smart_proj.Orchestrator.Orchestrator.Orchestrator.update(smart_proj.Orchestrator.Orchestrator.Orchestrator.
                                                                 getInstance(), sensor)
