# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def remove(self, item):
        valid_item = self.items.remove(item)

        if valid_item:
            print(f'You have removed {valid_item} from the room')
        else:
            print('There is no item by that name in the room')
