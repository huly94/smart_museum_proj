import logging

import statemachine

import smart_proj.Sensors.Sensor
import smart_proj.Apps.Observer

"""@package docstring
Documentation for this module.

An interactive painting is animated when a visitor is detected
it can be based on the emotions or the preferences of the user
"""


class InteractiveWorkMachine(smart_proj.Apps.Observer.Observer):
    wait = statemachine.State('Wait', initial=True)
    work_animated = statemachine.State('Work animated')

    animate_work = wait.to(work_animated)
    stop = work_animated.to(wait)

    actuator = None

    user = None

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def set_user(self, u):
        self.user = u

    def attach(self, paint):
        self.actuator = paint

    def on_animate_work(self):
        self.logger.info("Opera animata")
        self.actuator.turn_on()

    def on_stop(self):
        self.logger.info("Stop")
        self.actuator.turn_off()
        # when i turn the work off i set the user to -1 in order that the orchestrator remove the app
        self.set_user("-1")

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        self.logger.info("InteractiveWork received new sensor value:" + subject.current_state.name)
        if subject.user == self.user and subject.area == "Interactive work area":

            if "Empty" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    pass
                else:
                    self.stop()

            elif "Non Empty u18" == subject.current_state.name or "Non Empty o18" == subject.current_state.name:
                if "Wait" == self.current_state.name:
                    self.animate_work()
                else:
                    pass
