from statemachine import StateMachine
from smart_proj.Sensors import Sensor


class Observer(StateMachine):

    def update(self, subject: Sensor) -> None:
        pass
