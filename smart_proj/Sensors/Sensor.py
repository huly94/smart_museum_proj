import statemachine


class Sensor(statemachine.StateMachine):

    def __init__(self):
        super().__init__()
        self.area = ""

    def setArea(self, r):
        self.area = r

    # self._observers = []

    # def attach(self, observer):
    #     self._observers.append(observer)
    #
    # def detach(self, observer):
    #     self._observers.remove(observer)

    def notify(self):
        import smart_proj.Orchestrator.Orchestrator
        sensor = self
        smart_proj.Orchestrator.Orchestrator.Orchestrator.update(smart_proj.Orchestrator.Orchestrator.Orchestrator.
                                                                 getInstance(), sensor)
        # for observer in self._observers:
        #    observer.update(self)
