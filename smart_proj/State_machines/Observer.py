import statemachine
import smart_proj.Sensors


class Observer(statemachine.StateMachine):

    def update(self, subject: smart_proj.Sensors.Sensor) -> None:
        pass
