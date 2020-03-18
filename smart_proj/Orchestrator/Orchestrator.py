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
            if subject.area == "exit room":
                import smart_proj.State_machines.MobileSuggestionsMachine
                import smart_proj.Actuators.ActuatorMobile
                import smart_proj.Actuators.ActuatorLights
                import smart_proj.State_machines.LightsManagingMachine

                msm = smart_proj.State_machines.MobileSuggestionsMachine.MobileSuggestionsMachine()
                mobile = smart_proj.Actuators.ActuatorMobile.ActuatorMobile()
                msm.attach(mobile)
                self.attach(msm)
            elif subject.area == "interactive work":
                import smart_proj.Actuators.ActuatorPainting
                import smart_proj.State_machines.InteractiveWorkMachine
                import smart_proj.State_machines.AudioMusicRelaxMachine
                import smart_proj.Actuators.ActuatorAudio
                import smart_proj.Actuators.ActuatorLights
                import smart_proj.State_machines.LightsManagingMachine

                lmm_interactive = smart_proj.State_machines.LightsManagingMachine.LightsManagingMachine()
                light_interactive = smart_proj.Actuators.ActuatorLights.ActuatorLights()
                amr = smart_proj.State_machines.AudioMusicRelaxMachine.AudioMusicRelaxMachine()
                iwm = smart_proj.State_machines.InteractiveWorkMachine.InteractiveWorkMachine()
                painting = smart_proj.Actuators.ActuatorPainting.ActuatorPainting()
                audio_music = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()
                amr.attach(audio_music)
                iwm.attach(painting)
                lmm_interactive.attach(light_interactive)
                self.attach(iwm)
                self.attach(amr)
                self.attach(lmm_interactive)
            elif subject.area == "relax area":
                import smart_proj.State_machines.AudioMusicRelaxMachine
                import smart_proj.Actuators.ActuatorAudio
                import smart_proj.Actuators.ActuatorLights
                import smart_proj.State_machines.LightsManagingMachine

                audio_relax_machine = smart_proj.State_machines.AudioMusicRelaxMachine.AudioMusicRelaxMachine()
                audio_relax = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()
                manage_light_machine = smart_proj.State_machines.LightsManagingMachine.LightsManagingMachine()
                light_relax = smart_proj.Actuators.ActuatorLights.ActuatorLights()
                manage_light_machine.attach(light_relax)
                audio_relax_machine.attach(audio_relax)
                self.attach(audio_relax_machine)

            else:

                import smart_proj.State_machines.AudioMoreInformationsMachine
                import smart_proj.Actuators.ActuatorAudio
                import smart_proj.Actuators.ActuatorLights
                import smart_proj.State_machines.LightsManagingMachine

                ami = smart_proj.State_machines.AudioMoreInformationsMachine.AudioMoreInformationMachine()
                lvm = smart_proj.State_machines.LightsManagingMachine.LightsManagingMachine()
                light_visitor = smart_proj.Actuators.ActuatorLights.ActuatorLights()
                audio_more_info = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()
                lvm.attach(light_visitor)
                ami.attach(audio_more_info)
                self.attach(ami)
                self.attach(lvm)

        if s[0:s.index("(")] == "SensorWeather":
            import smart_proj.State_machines.LightsManagingMachine
            import smart_proj.Actuators.ActuatorLights

            lwm = smart_proj.State_machines.LightsManagingMachine.LightsManagingMachine()
            light_weather = smart_proj.Actuators.ActuatorLights.ActuatorLights()
            lwm.attach(light_weather)
            self.attach(lwm)

        if s[0:s.index("(")] == "SensorColors":
            import smart_proj.State_machines.PervasiveGameChromatizeIt
            import smart_proj.Actuators.ActuatorMobile
            import smart_proj.Actuators.ActuatorWall

            pgm = smart_proj.State_machines.PervasiveGameChromatizeIt.PervasiveGameChromatizeIt()
            mobile = smart_proj.Actuators.ActuatorMobile.ActuatorMobile()
            wall = smart_proj.Actuators.ActuatorWall.ActuatorWall()
            pgm.attach_mobile(mobile)
            pgm.attach_wall(wall)
            self.attach(pgm)

        if s[0:s.index("(")] == "SensorClock":
            import smart_proj.State_machines.LightsManagingMachine
            import smart_proj.Actuators.ActuatorLights

            lcm = smart_proj.State_machines.LightsManagingMachine.LightsManagingMachine()
            light_time = smart_proj.Actuators.ActuatorLights.ActuatorLights()
            lcm.attach(light_time)
            self.attach(lcm)

        if s[0:s.index("(")] == "SensorMobile":
            import smart_proj.State_machines.LightGiudeVisitorMachine
            import smart_proj.Actuators.ActuatorLights

            lgvm = smart_proj.State_machines.LightGiudeVisitorMachine.LightGuideVisitorMachine()
            light_guide = smart_proj.Actuators.ActuatorLights.ActuatorLights()
            lgvm.attach(light_guide)
            self.attach(lgvm)

        for observer in self._observers:
            observer.update(subject)
