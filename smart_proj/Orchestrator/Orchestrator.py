import logging
import smart_proj.Sensors.Sensor


# The class orchestrator is responsible of automatizing the assign process of sensors, app and actuators.
# It is based on a register in which we associate app to sensors and actuators to app. In this way the orchestrator
# is able to create an app when it receives a notification from a sensor. Also app triggered by the same sensor are
# divided in areas in order that the app is istantiated only when the visitor is in that area.
class Orchestrator:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Orchestrator.__instance is None:
            Orchestrator()
        return Orchestrator.__instance

    def __init__(self):
        import smart_proj.Apps.AudioVisitorApp
        import smart_proj.Apps.LightsManagingApp
        import smart_proj.Apps.InteractiveWorkApp
        import smart_proj.Apps.LightGiudeVisitorApp
        import smart_proj.Apps.AudioMusicRelaxApp
        import smart_proj.Apps.AudioMoreInformationsApp
        import smart_proj.Apps.MobileSuggestionsApp
        import smart_proj.Actuators.ActuatorAudio
        import smart_proj.Actuators.ActuatorLights
        import smart_proj.Actuators.ActuatorPainting
        import smart_proj.Actuators.ActuatorMobile
        import smart_proj.Apps.PervasiveGameChromatizeIt
        import smart_proj.Actuators.ActuatorWall

        lightApp = smart_proj.Apps.LightsManagingApp.LightsManagingMachine()
        ligths = smart_proj.Actuators.ActuatorLights.ActuatorLights()
        lightApp.attach(ligths)
        """ Virtually private constructor. """
        if Orchestrator.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Orchestrator.__instance = self
            # Since the light managing machine is the only app that is not dedicated to an exclusive user, we add it
            # in the observers list from the beginning
            self._observers = [lightApp]
            self.sensor_to_app = dict([
                ("SensorVisitorAge", [smart_proj.Apps.AudioVisitorApp.AudioVisitorMachine,
                                      smart_proj.Apps.AudioMoreInformationsApp.AudioMoreInformationMachine,
                                      smart_proj.Apps.AudioMusicRelaxApp.AudioMusicRelaxMachine,
                                      smart_proj.Apps.InteractiveWorkApp.InteractiveWorkMachine,
                                      smart_proj.Apps.MobileSuggestionsApp.MobileSuggestionsMachine]),
                ("SensorMobile", [smart_proj.Apps.LightGiudeVisitorApp.LightGuideVisitorMachine]),
                ("SensorColors", [smart_proj.Apps.PervasiveGameChromatizeIt.PervasiveGameChromatizeIt])
            ])
            self.app_to_actuators = dict([
                ("AudioVisitorMachine", [smart_proj.Actuators.ActuatorAudio.ActuatorAudio]),
                ("LightGuideVisitorMachine", [smart_proj.Actuators.ActuatorLights.ActuatorLights]),
                ("AudioMusicRelaxMachine", [smart_proj.Actuators.ActuatorAudio.ActuatorAudio]),
                ("AudioMoreInformationMachine", [smart_proj.Actuators.ActuatorAudio.ActuatorAudio]),
                ("InteractiveWorkMachine", [smart_proj.Actuators.ActuatorPainting.ActuatorPainting]),
                ("MobileSuggestionsMachine", [smart_proj.Actuators.ActuatorMobile.ActuatorMobile]),
                ("PervasiveGameChromatizeIt", [smart_proj.Actuators.ActuatorMobile.ActuatorMobile,
                                               smart_proj.Actuators.ActuatorWall.ActuatorWall])
            ])
            self.areas_to_app = dict([
                ("Exit area", ["MobileSuggestionsMachine"]),
                ("Relax area", ["AudioMusicRelaxMachine", "LightsManagingMachine"]),
                ("Works area", ["AudioVisitorMachine", "LightsManagingMachine", "LightGuideVisitorMachine",
                                "AudioMoreInformationMachine"]),
                ("Interactive work area", "InteractiveWorkMachine"),
                ("Game area", ["PervasiveGameChromatizeIt"])
                ])

    def exist_app_user(self, user):
        found = False
        for app in self._observers:
            if app.user == user.user and app.__class__ == user.__class__:
                found = True
                break
        return found

    # an app is removed from the observers list by the app itself when it is in its final state
    def remove_app(self, app):
        for obs in self._observers:
            if obs.user == app.user and obs.__class__ == app.__class__:
                self.detach(obs)

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def get_observers(self):
        return self._observers

    # The update method, basing on which sensor signal receives (if the sensor is not registered then it does nothing),
    # create an app and the actuator and link it to the correct user
    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("[ORCHESTRATOR]received update:" + subject.current_state.name)
        sensor_name = subject.__str__()  # i get the name of the sensor
        if sensor_name[0:sensor_name.index("(")] in self.sensor_to_app.keys():  # if the sensor exists in the register
            for app in self.sensor_to_app[sensor_name[0:sensor_name.index("(")]]:
                tmp = app()  # create the app
                app_name = tmp.__str__()  # i get the name of the app
                if app_name[0:app_name.index("(")] in self.areas_to_app[
                    subject.area]:  # if the app is in the area of the sensor
                    for act in self.app_to_actuators[app_name[0:app_name.index("(")]]:
                        act = act()
                        tmp.attach(act)  # i create the actuator and attach it
                        tmp.set_user(subject.user)  # i set the user
                    if not self.exist_app_user(tmp):  # i control if the app of this user already exists
                        self.attach(tmp)  # if not i attach it to the observers list

        for observer in self._observers:
            observer.update(subject) # i update all the observers, every app receives the sensor signal, but if it does
            # not match in its update method, the app does nothing
