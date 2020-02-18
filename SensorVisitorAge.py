from statemachine import State
from Sensor import Sensor


class SensorVisitorAge(Sensor):
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
        print("A new visitor u18 has arrived, new state:", self.current_state.name)
        self.notify()

    def on_enter_non_empty_o18(self):
        print("A new visitor o18 has arrived, new state:", self.current_state.name)
        self.notify()

    def on_enter_empty(self):
        print("Visitor has left, new state:", self.current_state.name)
        self.notify()


