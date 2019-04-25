# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.current_room = current_room
        self.location = current_room.name
        self.name = name
        self.inventory = []

    def get_room(self):
        return self.current_room

    def change_room(self, direction):
        # path = direction[0] + '_to'
        if direction == 'north':
            self.current_room = self.current_room.n_to
        elif direction == 'south':
            self.current_room = self.current_room.s_to
        elif direction == 'east':
            self.current_room = self.current_room.e_to
        elif direction == 'west':
            self.current_room = self.current_room.w_to
        # if self.current_room[path] == None:
        #     print(f"{direction} is not a valid direction")
        # self.current_room = self.current_room[path]

    # def pick_up(self, item_name):
    #     room = self.current_room
    #     item = room.get_item(item_name)
    #     self.inventory.append(item)

    # def drop(self, item_name):
    #     item = self.get_item(item_name)

    #     self.inventory.remove(item)

    def get_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return item
