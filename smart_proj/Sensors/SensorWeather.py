import logging
import statemachine
import smart_proj.Sensors.Sensor


class SensorWeather(smart_proj.Sensors.Sensor.Sensor):
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    sunny = statemachine.State('Sunny', initial=True)
    cloud = statemachine.State('Cloud')

    bad_weather = sunny.to(cloud)
    good_weather = cloud.to(sunny)

    def __init__(self):
        super().__init__()

    def on_enter_cloud(self):
        logging.info("[SENSOR WEATHER]: Clouds arrived, new state:" + self.current_state.name)
        self.notify()

    def on_enter_sunny(self):
        logging.info("[SENSOR WEATHER]: Sun arrived, new state:" + self.current_state.name)
        self.notify()
