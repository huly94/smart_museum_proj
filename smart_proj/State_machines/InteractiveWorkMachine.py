from statemachine import State

from smart_proj.Sensors.Sensor import Sensor
from smart_proj.State_machines.Observer import Observer


class InteractiveWorkMachine(Observer):
    wait = State('Wait', initial=True)
    work_animated = State('Work animated')

    animate_work = wait.to(work_animated)
    stop = work_animated.to(wait)

    actuator = None

    def attach_painting(self, paint):
        self.actuator = paint

    def on_animate_work(self):
        print("Opera animata")
        self.actuator.turn_on()

    def on_stop(self):
        print("Stop")
        self.actuator.turn_off()

    def update(self, subject: Sensor):
        print("InteractiveWork received new sensor value", subject.current_state.name)
        if "Empty" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                pass
            else:
                self.stop()

        elif "Non Empty" == subject.current_state.name:
            if "Wait" == self.current_state.name:
                self.animate_work()
            else:
                pass
