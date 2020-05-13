import logging
import smart_proj.Sensors.Sensor
import smart_proj.Actuators.Actuator
import smart_proj.Apps.App


# The class orchestrator is responsible of automatizing the assign process of sensors, app and actuators.
# It is based on a register in which we associate app to sensors and actuators to app. In this way the orchestrator
# is able to create an app when it receives a notification from a sensor. Also app triggered by the same sensor are
# divided in areas in order that the app is istantiated only when the visitor is in that area.
class Orchestrator:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Orchestrator.__instance is None:
            Orchestrator()
        return Orchestrator.__instance

    def __init__(self):

        """ Virtually private constructor. """
        if Orchestrator.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Orchestrator.__instance = self
            self._observers = []
            self.sensors = []
            self.actuators = []
            self.sensor_to_app = {}
            self.app_to_actuators = {}
            self.areas_to_app = {}
            self.logger = logging.getLogger(self.__class__.__name__)
            self.app_to_typology = {}

    def register_sensor(self, this_sensor: smart_proj.Sensors.Sensor.Sensor):
        self.sensors.append(type(this_sensor))

    def register_actuator(self, this_actuator: smart_proj.Actuators.Actuator.Actuator):
        self.actuators.append(type(this_actuator))

    def register_area(self, this_app: smart_proj.Apps.App.App, area: str):
        app_name = this_app.__str__()
        name = app_name[0:app_name.index("(")]
        if area in self.areas_to_app.keys():
            self.areas_to_app[area].append(name)
        else:
            self.areas_to_app[area] = []
            self.areas_to_app[area].append(name)

    def register_typology(self, app: smart_proj.Apps.App.App, typology: str):
        app_name = app.__str__()
        name = app_name[0:app_name.index("(")]
        self.app_to_typology[name] = typology
        if typology == "General":
            for act in self.app_to_actuators[name]:
                act = act()
                app.attach(act)  # i create the actuator and attach it
            self._observers.append(app)

    def register_app(self, this_app: smart_proj.Apps.App.App):
        deps_sensor = this_app.dependencies_sensors()
        deps_actuator = this_app.dependencies_actuators()
        for sensor in deps_sensor:
            if sensor in self.sensors:
                sensor_name = sensor().__str__()
                name = sensor_name[0:sensor_name.index("(")]
                if name in self.sensor_to_app.keys():
                    self.sensor_to_app[name].append(type(this_app))
                else:
                    self.sensor_to_app[name] = []
                    self.sensor_to_app[name].append(type(this_app))
            else:
                raise Exception('Sensor Not Supported',
                                'Sensor type ' + str(sensor) + ' is not supported by the orchestrator')
        for actuator in deps_actuator:
            if actuator in self.actuators:
                app_name = this_app.__str__()
                name = app_name[0:app_name.index("(")]
                if name in self.app_to_actuators.keys():
                    self.app_to_actuators[name].append(actuator)
                else:
                    self.app_to_actuators[name] = []
                    self.app_to_actuators[name].append(actuator)
            else:
                raise Exception('Actuator Not Supported',
                                'Actuator type ' + str(actuator) + ' is not supported by the orchestrator')

    def exist_app_user(self, user):
        found = False
        for app in self._observers:
            if app.user == user.user and app.__class__ == user.__class__:
                found = True
                break
        return found

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def get_observers(self):
        return self._observers

    # The update method, basing on which sensor signal receives (if the sensor is not registered then it does nothing),
    # create an app and the actuator and link it to the correct user
    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        self.logger.info("received update:" + subject.current_state.name)
        sensor_name = subject.__str__()  # i get the name of the sensor
        if sensor_name[0:sensor_name.index("(")] in self.sensor_to_app.keys():  # if the sensor exists in the register
            for app in self.sensor_to_app[sensor_name[0:sensor_name.index("(")]]:
                tmp = app()  # create the app
                app_name = tmp.__str__()  # i get the name of the app
                if self.app_to_typology[app_name[0:app_name.index("(")]] == "Individual":
                    if app_name[0:app_name.index("(")] in self.areas_to_app[subject.area]:  # if the app is in the area of the sensor
                        for act in self.app_to_actuators[app_name[0:app_name.index("(")]]:
                            act = act()
                            tmp.attach(act)  # i create the actuator and attach it
                            tmp.set_user(subject.user)  # i set the user
                        if not self.exist_app_user(tmp):  # i control if the app of this user already exists
                            self.attach(tmp)  # if not i attach it to the observers list

        # Updating phase
        for observer in self._observers:
            observer.update(subject)  # i update all the observers, every app receives the sensor signal, but if it does
            # not match in its update method, the app does nothing
        # Deleting phase
        i = 0
        while i < len(self._observers):
            obs = self._observers[i]
            if obs.user == "-1":
                self.detach(obs)
                i -= 1
            i += 1
