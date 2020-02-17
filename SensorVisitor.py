from statemachine import State

from Sensor import Sensor


class SensorVisitor(Sensor):
    empty = State('Empty', initial=True)
    non_empty = State('Non Empty')

    visitor_arrived = empty.to(non_empty)
    visitor_left = non_empty.to(empty)

    def __init__(self):
        super().__init__()

    def on_enter_non_empty(self):
        print("A new visitor has arrived, new state:", self.current_state.name)
        self.notify()

    def on_enter_empty(self):
        print("Visitor has left, new state:", self.current_state.name)
        self.notify()
