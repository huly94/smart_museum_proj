import random
import simulation.Room


class Visitor:
    def __init__(self):
        self.age = random.randint(6, 80)
        self.room = None
        self.position = None
        self.tag = None

    def get_age(self):
        return self.age

    def enter_in_room(self, room):
        if self.room is not None:
            self.room.people_in_room.remove(self)
        self.room = room
        room.add_person_in_room(self)

    def move_to_pos(self, new_position):
        if new_position in self.room.point_to_areas.keys():
            if self.position is not None:
                self.room.people_at_point[self.position].remove(self)
            self.position = new_position
            self.room.add_person_at_point(self, new_position)

    def __str__(self) -> str:
        return "Age of the visitor: " + str(self.age) + ", at position: " + str(self.position)
