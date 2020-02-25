import logging

from statemachine import State

from smart_proj.Sensors.Sensor import Sensor
from smart_proj.State_machines.Observer import Observer


class AudioMoreInformationMachine(Observer):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    wait = State('Wait', initial=True)
    more_info_provided = State('More informations provided')

    play_another_track = wait.to(more_info_provided)
    turn_off = more_info_provided.to(wait)

    visitor = False

    actuator = None

    def attach_audio(self, audio):
        self.actuator = audio

    def on_play_another_track(self):
        logging.info("Time out, riproduco un'altra traccia")
        self.actuator.turn_on()

    def on_turn_off(self):
        logging.info("Spento")
        self.actuator.turn_off()

    def update(self, subject: Sensor):
        logging.info("AudioMoreInformation recieved a new sensor value:" + subject.current_state.name)
        if "Empty" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                self.visitor = False
                logging.info("no extra audio")
            elif self.visitor:
                self.turn_off()
                self.visitor = False
            else:
                pass

        elif "Non Empty" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                self.visitor = True
                logging.info("Waiting for timer...")
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




