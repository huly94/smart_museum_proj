import simulation.Visitor
import smart_proj.Orchestrator.Orchestrator
import simulation.Room
import random
import smart_proj.Sensors.SensorVisitorAge
import smart_proj.Apps.AudioVisitorApp
import smart_proj.Apps.MobileSuggestionsApp
import smart_proj.Apps.InteractiveWorkApp
import smart_proj.Apps.AudioMusicRelaxApp
import smart_proj.Apps.AudioMoreInformationsApp
import smart_proj.Apps.LightsManagingApp
import smart_proj.Sensors.SensorTimer
import smart_proj.Sensors.SensorClock
import smart_proj.Sensors.SensorWeather
import smart_proj.Sensors.SensorPresence
import smart_proj.Sensors.SensorMobile
import smart_proj.Actuators.ActuatorAudio
import smart_proj.Actuators.ActuatorMobile
import smart_proj.Actuators.ActuatorLights
import smart_proj.Actuators.ActuatorPainting


if __name__ == '__main__':

    # Initialize Room
    # Assume that we have only 1 room.
    # In this example, all sensors/actuators refer to the same room.
    r1 = simulation.Room.Room()

    # Step 1: Initialize orchestrator
    my_orchestrator = smart_proj.Orchestrator.Orchestrator.Orchestrator()

    # Step 2.2: Initialize sensors available in the room
    sensor_visitor_age = smart_proj.Sensors.SensorVisitorAge.SensorVisitorAge()
    sensor_timer = smart_proj.Sensors.SensorTimer.SensorTimer()
    sensor_clock = smart_proj.Sensors.SensorClock.SensorClock()
    sensor_weather = smart_proj.Sensors.SensorWeather.SensorWeather()
    sensor_presence = smart_proj.Sensors.SensorPresence.SensorPresence()
    sensor_mobile = smart_proj.Sensors.SensorMobile.SensorMobile()

    # Step 2.3: Register sensors to orchestrator
    my_orchestrator.register_sensor(sensor_visitor_age)
    my_orchestrator.register_sensor(sensor_timer)
    my_orchestrator.register_sensor(sensor_clock)
    my_orchestrator.register_sensor(sensor_weather)
    my_orchestrator.register_sensor(sensor_presence)
    my_orchestrator.register_sensor(sensor_mobile)

    # Step 2.4: Initialize actuators available in the room
    audio = smart_proj.Actuators.ActuatorAudio.ActuatorAudio()
    light = smart_proj.Actuators.ActuatorLights.ActuatorLights()
    mobile = smart_proj.Actuators.ActuatorMobile.ActuatorMobile()
    painting = smart_proj.Actuators.ActuatorPainting.ActuatorPainting()

    # Step 2.5: Register actuators to orchestrator
    my_orchestrator.register_actuator(audio)
    my_orchestrator.register_actuator(light)
    my_orchestrator.register_actuator(mobile)
    my_orchestrator.register_actuator(painting)

    # Step 3.1: Initialize Application
    audio_visitor_app = smart_proj.Apps.AudioVisitorApp.AudioVisitorMachine()
    audio_more_info_app = smart_proj.Apps.AudioMoreInformationsApp.AudioMoreInformationMachine()
    light_managing_app = smart_proj.Apps.LightsManagingApp.LightsManagingMachine()
    mobile_suggestion_app = smart_proj.Apps.MobileSuggestionsApp.MobileSuggestionsMachine()
    audio_music_relax_app = smart_proj.Apps.AudioMusicRelaxApp.AudioMusicRelaxMachine()
    interactive_work_app = smart_proj.Apps.InteractiveWorkApp.InteractiveWorkMachine()

    # Step 3.1.1: Set the typology of the app
    audio_visitor_app.set_typology("Individual")
    audio_more_info_app.set_typology("Individual")
    mobile_suggestion_app.set_typology("Individual")
    audio_music_relax_app.set_typology("Individual")
    interactive_work_app.set_typology("Individual")
    light_managing_app.set_typology("General")

    # Step 3.2: Register App to orchestrator
    my_orchestrator.register_app(audio_visitor_app)
    my_orchestrator.register_app(audio_more_info_app)
    my_orchestrator.register_app(audio_music_relax_app)
    my_orchestrator.register_app(light_managing_app)
    my_orchestrator.register_app(mobile_suggestion_app)
    my_orchestrator.register_app(interactive_work_app)

    # Step 3.3: Register the Area of the app to the orchestrator
    my_orchestrator.register_area(audio_music_relax_app, "Relax area")
    my_orchestrator.register_area(audio_visitor_app, "Works area" )
    my_orchestrator.register_area(audio_more_info_app, "Works area" )
    my_orchestrator.register_area(mobile_suggestion_app, "Exit area")
    my_orchestrator.register_area(interactive_work_app, "Interactive work area")

    # Add point of interest inside the room.
    # Associate to each point of interest the type of area
    r1.add_point_of_interest("Bench", "Relax area")
    r1.add_point_of_interest("Gioconda", "Works area")
    r1.add_point_of_interest("Exit1", "Exit area")
    r1.add_point_of_interest("Picasso", "Works area")
    r1.add_point_of_interest("Dali'", "Works area")
    r1.add_point_of_interest("Animated Opera", "Interactive work area")

    # Associate a sensor to each point of interest
    r1.add_sensor_at_point("RFID reader", "Gioconda")
    r1.add_sensor_at_point("Sensor timer", "Gioconda")
    r1.add_sensor_at_point("RFID reader", "Picasso")
    r1.add_sensor_at_point("Sensor timer", "Picasso")
    r1.add_sensor_at_point("RFID reader", "Dali'")
    r1.add_sensor_at_point("Sensor timer", "Dali'")
    r1.add_sensor_at_point("RFID reader", "Bench")
    r1.add_sensor_at_point("RFID reader", "Exit1")
    r1.add_sensor_at_point("RFID reader", "Animated Opera")

    # this are the tags we associate to each visitor
    # they represent the tag attached to the audio guide that is detected by the RFID reader
    id_u18 = 100
    id_o18 = 200

    # instantiate a random number of visitor, and give to them a tag basing on the age
    nr_of_visitors = random.randint(1, 10)
    print("The number of visitors is: ", str(nr_of_visitors))
    visitors = []
    for i in range(0, nr_of_visitors):
        tmp = simulation.Visitor.Visitor()
        print(tmp.get_age())
        if tmp.get_age() > 18:
            tmp.tag = id_o18
            id_o18 += 1
        else:
            tmp.tag = id_u18
            id_u18 += 1
        tmp.enter_in_room(r1)

    visitors = r1.people_in_room
    points = list(r1.point_to_areas.keys())
    for i in range(0, 10):
        for v in visitors:
            v.move_to_pos(points[random.randint(0, len(points) - 1)])
            r1.update()
        print(r1.people_at_point)
    print(r1.time)

    print("Active processes: ", my_orchestrator.users_active_processes)
    print("History of processes: ", my_orchestrator.user_history)
    print("Visitors: ", my_orchestrator.visitors)
