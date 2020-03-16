import logging
import smart_proj.Orchestrator.Singleton
import smart_proj.Sensors.Sensor


class Orchestrator(smart_proj.Orchestrator.Singleton.Singleton):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    def __init__(self):
        super().__init__()

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        logging.info("[ORCHESTRATOR]recived update:" + subject.current_state.name)
        s = subject.__str__()
        if s[0:s.index("(")] == "SensorVisitorAge":
            import smart_proj.State_machines.AudioVisitorMachine
            import smart_proj.Actuators.ActuatorAudio
            import smart_proj.Actuators.ActuatorLights
            import smart_proj.State_machines.LightsManagingMachine
            avm = smart_proj.State_machines.AudioVisitorMachine.AudioVisitorMachine()
            lmm = smart_proj.State_machines.LightsManagingMachine.LightsManagingMachine()
            light = smart_proj.Actuators.ActuatorLights.ActuatorLights()
            audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()
            lmm.attach(light)
            avm.attach(audio)
            self.attach(lmm)
            self.attach(avm)
        if s[0:s.index("(")] == "SensorVisitor":
            import smart_proj.State_machines.AudioMoreInformationsMachine
            import smart_proj.Actuators.ActuatorAudio
            ami = smart_proj.State_machines.AudioMoreInformationsMachine.AudioMoreInformationMachine()
            audio_more_info = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()
            ami.attach(audio_more_info)
            self.attach(ami)

        for observer in self._observers:
            observer.update(subject)
