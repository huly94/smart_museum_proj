import logging
import smart_proj.Orchestrator.Singleton
import smart_proj.Sensors.Sensor


class Orchestrator(smart_proj.Orchestrator.Singleton.Singleton):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    def __init__(self):

        super().__init__()

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("[ORCHESTRATOR]received update:" + subject.current_state.name)
        s = subject.__str__()
        if s[0:s.index("(")] in self.sensor_to_app.keys():
            for app in self.sensor_to_app[s[0:s.index("(")]]:
                tmp = app()
                s_app = tmp.__str__()
                if s_app[0:s_app.index("(")] in self.areas_to_app[subject.area]:
                    act = self.app_to_actuators[s_app[0:s_app.index("(")]]()
                    tmp.attach(act)
                    tmp.set_user(subject.user)
                    if not self.exist_app_user(tmp):
                        self.attach(tmp)

        for observer in self._observers:
            observer.update(subject)


