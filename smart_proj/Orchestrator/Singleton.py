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
        import smart_proj.State_machines.AudioVisitorMachine
        import smart_proj.State_machines.LightsManagingMachine
        import smart_proj.State_machines.InteractiveWorkMachine
        import smart_proj.State_machines.LightGiudeVisitorMachine
        import smart_proj.State_machines.AudioMusicRelaxMachine
        import smart_proj.State_machines.AudioMoreInformationsMachine
        import smart_proj.State_machines.MobileSuggestionsMachine
        import smart_proj.Actuators.ActuatorAudio
        import smart_proj.Actuators.ActuatorLights
        import smart_proj.Actuators.ActuatorPainting
        import smart_proj.Actuators.ActuatorMobile

        lightApp = smart_proj.State_machines.LightsManagingMachine.LightsManagingMachine()
        ligths = smart_proj.Actuators.ActuatorLights.ActuatorLights()
        lightApp.attach(ligths)
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
            self._observers = [lightApp]
            self.sensor_to_app = dict([
                ("SensorVisitorAge", [smart_proj.State_machines.AudioVisitorMachine.AudioVisitorMachine]),
                ("SensorMobile", [smart_proj.State_machines.LightGiudeVisitorMachine.LightGuideVisitorMachine]),
                ("SensorVisitor", [smart_proj.State_machines.AudioMusicRelaxMachine.AudioMusicRelaxMachine,
                                   smart_proj.State_machines.AudioMoreInformationsMachine.AudioMoreInformationMachine,
                                   smart_proj.State_machines.InteractiveWorkMachine.InteractiveWorkMachine,
                                   smart_proj.State_machines.MobileSuggestionsMachine.MobileSuggestionsMachine])
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

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def update(self, sensor: smart_proj.Sensors.Sensor.Sensor) -> None:
        pass

