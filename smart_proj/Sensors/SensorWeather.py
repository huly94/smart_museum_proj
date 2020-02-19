from statemachine import State
from smart_proj.Sensors.Sensor import Sensor


class SensorWeather(Sensor):
    sunny = State('Sunny', initial=True)
    cloud = State('Cloud')

    bad_weather = sunny.to(cloud)
    good_weather = cloud.to(sunny)

    def __init__(self):
        super().__init__()

    def on_enter_cloud(self):
        print("Clouds arrived, new state:", self.current_state.name)
        self.notify()

    def on_enter_sunny(self):
        print("Sun arrived, new state:", self.current_state.name)
        self.notify()
