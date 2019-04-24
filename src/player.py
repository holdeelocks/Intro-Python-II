# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.current_room = current_room
        self.name = name
        self.inventory = []

    def get_room(self):
        return self.current_room

    def change_room(self, new_room):
        self.current_room = new_room
