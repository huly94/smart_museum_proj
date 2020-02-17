from statemachine import StateMachine


class Sensor(StateMachine):

    def __init__(self):
        super().__init__()
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)
