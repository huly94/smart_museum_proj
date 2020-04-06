import smart_proj.Sensors.Sensor


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

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

        lightApp = smart_proj.Apps.LightsManagingApp.LightsManagingMachine()
        ligths = smart_proj.Actuators.ActuatorLights.ActuatorLights()
        lightApp.attach(ligths)
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
            self._observers = [lightApp]
            self.sensor_to_app = dict([
                ("SensorVisitorAge", [smart_proj.Apps.AudioVisitorApp.AudioVisitorMachine]),
                ("SensorMobile", [smart_proj.Apps.LightGiudeVisitorApp.LightGuideVisitorMachine]),
                ("SensorVisitor", [smart_proj.Apps.AudioMusicRelaxApp.AudioMusicRelaxMachine,
                                   smart_proj.Apps.AudioMoreInformationsApp.AudioMoreInformationMachine,
                                   smart_proj.Apps.InteractiveWorkApp.InteractiveWorkMachine,
                                   smart_proj.Apps.MobileSuggestionsApp.MobileSuggestionsMachine])
            ])
            self.app_to_actuators = dict([
                ("AudioVisitorMachine", smart_proj.Actuators.ActuatorAudio.ActuatorAudio),
                ("LightGuideVisitorMachine", smart_proj.Actuators.ActuatorLights.ActuatorLights),
                ("AudioMusicRelaxMachine", smart_proj.Actuators.ActuatorAudio.ActuatorAudio),
                ("AudioMoreInformationMachine", smart_proj.Actuators.ActuatorAudio.ActuatorAudio),
                ("InteractiveWorkMachine", smart_proj.Actuators.ActuatorPainting.ActuatorPainting),
                ("MobileSuggestionsMachine", smart_proj.Actuators.ActuatorMobile.ActuatorMobile)
            ])
            self.areas_to_app = dict([
                ("Exit area", ["MobileSuggestionsMachine"]),
                ("Relax area", ["AudioMusicRelaxMachine", "LightsManagingMachine"]),
                ("Works area", ["AudioVisitorMachine", "LightsManagingMachine", "LightGuideVisitorMachine",
                                "AudioMoreInformationMachine"]),
                ("Interactive work area", "InteractiveWorkMachine")

            ])

    def exist_app_user(self, user):
        found = False
        for app in self._observers:
            if app.user == user.user and app.__class__ == user.__class__:
                found = True
                break
        return found

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

    def update(self, sensor: smart_proj.Sensors.Sensor.Sensor) -> None:
        pass

