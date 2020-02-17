from statemachine import State
from Sensor import Sensor



class SensorVisitorAge(Sensor):
    empty = State('Empty')


    def __init__(self):
        super().__init__()


