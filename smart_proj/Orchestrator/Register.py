
class Register:
    sensor_to_statemachines = dict([
        ("SensorClock", ["LightsManagingMachine"]),
        ("SensorColors", ["PervasiveGameChromatizeIt"]),
        ("SensorGesture", ["PervasiveGameChromatizeIt"]),
        ("SensorMobile", ["LightGuideVisitorMachine"]),
        ("SensorTimer", ["AudioMoreInformationMachine"]),
        ("SensorVisitor", ["AudioMusicRelaxMachine", "AudioMoreInformationMachine", "InteractiveWorkMachine",
                         "MobileSuggestionsMachine"]),
        ("SensorVisitorAge", ["AudioVisitorMachine"]),
        ("SensorWeather", ["LightsManagingMachine"])
    ])

    statemachine_to_actuators = dict([
        ("LightsManagingMachine", ["ActuatorLights"]),
        ("AudioMoreInformationMachine", ["ActuatorAudio"]),
        ("AudioMusicRelaxMachine", ["ActuatorAudio"]),
        ("InteractiveWorkMachine", ["ActuatorPainting"]),
        ("LightGuideVisitorMachine", ["ActuatorLights"]),
        ("MobileSuggestionsMachine", ["ActuatorMobile"]),
        ("AudioVisitorMachine", ["ActuatorAudio"]),
        ("PervasiveGameChromatizeIt", ["ActuatorMobile" ,"ActuatorWall"])

    ])
