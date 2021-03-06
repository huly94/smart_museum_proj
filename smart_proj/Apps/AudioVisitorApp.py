import logging
import smart_proj.Sensors.Sensor
import smart_proj.Apps.App
import statemachine

"""@package docstring
Documentation for this module.

Basing on the age of the visitor, a certain audio track is played. 
the audio is transmitted on the audio-guide headphones of the visitor
"""


class AudioVisitorMachine(smart_proj.Apps.App.App):
    wait = statemachine.State('Wait', initial=True)
    playing_track_u18 = statemachine.State('Playing track for u18')
    playing_track_o18 = statemachine.State('Playing track for o18')

    play_track_u18 = wait.to(playing_track_u18)
    turn_off_track_u18 = playing_track_u18.to(wait)
    play_track_o18 = wait.to(playing_track_o18)
    turn_off_track_o18 = playing_track_o18.to(wait)

    actuator = None
    user = None

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def set_user(self, u):
        if self.typology == "General":
            raise Exception("Cannot define a user for a general app!")
        elif self.typology == "Individual":
            self.user = u

    def dependencies_sensors(self) -> []:
        import smart_proj.Sensors.SensorVisitorAge
        return [smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge]

    def dependencies_actuators(self) -> []:
        import smart_proj.Actuators.ActuatorAudio
        return [smart_proj.Actuators.ActuatorAudio.ActuatorAudio]

    def attach(self, audio):
        self.actuator = audio

    def on_play_track_u18(self):
        self.logger.info("Playing track for u18")
        self.actuator.turn_on()

    def on_turn_off_track_u18(self):
        self.logger.info("Turning off")
        self.actuator.turn_off()
        # when i turn the audio off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def on_play_track_o18(self):
        self.logger.info("Playing track for o18")
        self.actuator.turn_on()

    def on_turn_off_track_o18(self):
        self.logger.info("Turning off")
        self.actuator.turn_off()
        app = self
        # when i turn the audio off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        self.logger.info("AudioVisitor received new sensor value:" + subject.current_state.name)
        if subject.user == self.user:
            if "Empty" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    pass
                else:
                    try:
                        self.turn_off_track_o18()
                    except:
                        self.turn_off_track_u18()

            elif "Non Empty u18" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    self.play_track_u18()
                else:
                    pass

            elif "Non Empty o18" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    self.play_track_o18()
                else:
                    pass
