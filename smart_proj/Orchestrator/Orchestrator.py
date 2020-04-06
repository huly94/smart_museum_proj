import logging
import smart_proj.Orchestrator.Singleton
import smart_proj.Sensors.Sensor


class Orchestrator(smart_proj.Orchestrator.Singleton.Singleton):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    def __init__(self):
        super().__init__()

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("[ORCHESTRATOR]received update:" + subject.current_state.name)
        sensor_name = subject.__str__()  # i get the name of the sensor
        if sensor_name[0:sensor_name.index("(")] in self.sensor_to_app.keys():    # if the sensor exists in the register
            for app in self.sensor_to_app[sensor_name[0:sensor_name.index("(")]]:
                tmp = app()  # create the app
                app_name = tmp.__str__()  # i get the name of the app
                if app_name[0:app_name.index("(")] in self.areas_to_app[subject.area]:  # if the app is in the area of the sensor
                    act = self.app_to_actuators[app_name[0:app_name.index("(")]]()
                    tmp.attach(act)   # i create the actuator and attach it
                    tmp.set_user(subject.user)  # i set the user
                    if not self.exist_app_user(tmp):  # i control if the app of this user already exists
                        self.attach(tmp)  # if not i attach it to the observers list

        for observer in self._observers:
            observer.update(subject)  # i update all the observers
