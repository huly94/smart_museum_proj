import logging
import statemachine
import smart_proj.Sensors.Sensor
import smart_proj.Apps.App

"""@package docstring
Documentation for this module.

A visitor receives more information 
about a work if he spends more time after the end of the track
another track is played in which he receives more information

"""


class AudioMoreInformationMachine(smart_proj.Apps.App.App):
    wait = statemachine.State('Wait', initial=True)
    more_info_provided = statemachine.State('More informations provided')

    play_another_track = wait.to(more_info_provided)
    turn_off = more_info_provided.to(wait)

    visitor = False

    actuator = None

    user = None

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def dependencies_sensors(self) -> []:
        import smart_proj.Sensors.SensorVisitorAge
        import smart_proj.Sensors.SensorTimer
        return [smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge, smart_proj.Sensors.SensorTimer.SensorTimer]

    def dependencies_actuators(self) -> []:
        import smart_proj.Actuators.ActuatorAudio
        return [smart_proj.Actuators.ActuatorAudio.ActuatorAudio]

    def set_user(self, u):
        self.user = u

    def attach(self, audio):
        self.actuator = audio

    def on_play_another_track(self):
        self.logger.info("Time out, riproduco un'altra traccia")
        self.actuator.turn_on()

    def on_turn_off(self):
        self.logger.info("Spento")
        self.actuator.turn_off()
        # when i turn the audio off  i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        self.logger.info("AudioMoreInformation received a new sensor value:" + subject.current_state.name)
        if subject.user == self.user and subject.area == "Works area":
            if "Empty" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    self.visitor = False
                    self.logger.info("no extra audio")
                    # when i turn the audio off  i set the user to -1 in order that the orchestrator remove the app
                    self.set_user("-1")
                elif self.visitor:
                    self.turn_off()
                    self.visitor = False
                else:
                    pass

            elif "Non Empty u18" == subject.current_state.name or "Non Empty o18" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    self.visitor = True
                    self.logger.info("Waiting for timer...")
                else:
                    pass

            elif "Timer waiting" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    pass
                else:
                    self.turn_off()
                    self.visitor = False

            elif "Timer expired" == subject.current_state.name:
                if "Wait" == self.current_state.name and self.visitor:
                    self.play_another_track()
                else:
                    pass
