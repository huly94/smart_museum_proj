import simulation.Visitor
import simulation.Room
import random

if __name__ == '__main__':

    # Initialize Room
    # Assume that we have only 1 room.
    # In this example, all sensors/actuators refer to the same room.
    r1 = simulation.Room.Room()

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
    for i in range(0, 2):
        for v in visitors:
            v.move_to_pos(points[random.randint(0, len(points) - 1)])
            r1.update()
        print(r1.people_at_point)
    print(r1.time)
