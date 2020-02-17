from statemachine import StateMachine
import Sensor


class Observer(StateMachine):

    def update(self, subject: Sensor) -> None:
        pass
