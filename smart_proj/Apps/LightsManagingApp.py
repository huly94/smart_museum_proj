import logging

import smart_proj.Apps.App
import smart_proj.Sensors.Sensor
import statemachine

"""@package docstring
Documentation for this module.

The lights turn on or off basing on time, weather or visitor presence 
"""


class LightsManagingMachine(smart_proj.Apps.App.App):
    lights_off = statemachine.State('Lights off', initial=True)
    lights_on_for_visitors = statemachine.State('Lights on for visitors')
    lights_on_for_clouds = statemachine.State('Lights on for clouds')
    lights_on_for_night = statemachine.State('Lights on for night')

    turn_the_lights_on_visitor = lights_off.to(lights_on_for_visitors)
    turn_the_lights_off_visitor = lights_on_for_visitors.to(lights_off) | lights_on_for_clouds.to(lights_off) | \
                                  lights_on_for_night.to(lights_off)
    turn_the_lights_on_clouds = lights_off.to(lights_on_for_clouds)
    turn_the_lights_off_clouds = lights_on_for_clouds.to(lights_off)
    turn_the_lights_on_night = lights_off.to(lights_on_for_night)
    turn_the_lights_off_night = lights_on_for_night.to(lights_off)

    actuator = None
    user = None

    night = False
    cloud = False

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(self.__class__.__name__)

    def attach(self, lights):
        self.actuator = lights

    def dependencies_sensors(self) -> []:
        import smart_proj.Sensors.SensorPresence
        import smart_proj.Sensors.SensorClock
        import smart_proj.Sensors.SensorWeather
        return [smart_proj.Sensors.SensorClock.SensorClock, smart_proj.Sensors.SensorWeather.SensorWeather,
                smart_proj.Sensors.SensorPresence.SensorPresence]

    def dependencies_actuators(self) -> []:
        import smart_proj.Actuators.ActuatorLights
        return [smart_proj.Actuators.ActuatorLights.ActuatorLights]

    def on_turn_the_lights_on_visitor(self):
        self.logger.info("luci accese per visitatore")
        self.actuator.turn_on()

    def on_turn_the_lights_off_visitor(self):
        self.logger.info("luci spente per visitatore")
        self.actuator.turn_off()

    def on_turn_the_lights_on_clouds(self):
        self.logger.info("luci accese per nuvole")
        self.cloud = True
        self.actuator.turn_on()

    def on_turn_the_lights_off_clouds(self):
        self.logger.info("luci spente per nuvole")
        self.cloud = False
        self.actuator.turn_off()

    def on_turn_the_lights_on_night(self):
        self.logger.info("luci accese notte")
        self.night = True
        self.actuator.turn_on()

    def on_turn_the_lights_off_night(self):
        self.logger.info("luci spente")
        self.night = False
        self.actuator.turn_off()

    def update(self, subject: smart_proj.Sensors.Sensor.Sensor):
        self.logger.info("LightsManaging received new sensor value:" + subject.current_state.name)
        if 'Not detected' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                pass
            else:
                self.turn_the_lights_off_visitor()

        elif 'Person detected' == subject.current_state.name or 'Non Empty u18' == subject.current_state.name \
                or 'Non Empty o18' == subject.current_state.name:
            if 'Lights off' == self.current_state.name and self.night:
                self.turn_the_lights_on_visitor()
            else:
                pass

        elif 'Sunny' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                pass
            else:
                self.turn_the_lights_off_clouds()

        elif 'Cloud' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                self.turn_the_lights_on_clouds()
            else:
                pass

        elif 'Morning' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                pass
            else:
                self.turn_the_lights_off_night()

        elif 'Night' == subject.current_state.name:
            if 'Lights off' == self.current_state.name:
                self.turn_the_lights_on_night()
            else:
                pass
