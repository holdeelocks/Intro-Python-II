# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.current_room = current_room
        self.name = name
        self.inventory = []

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        valid_item = self.inventory.remove(item)

        if valid_item:
            print('That item has been removed')
        else:
            print("You can't drop an item you don't have!")
