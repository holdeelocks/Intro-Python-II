# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item

    def add_item(self, item):
        self.items.append(item)

    def remove(self, item_name):
        item = self.get_item(item_name)

        self.items.remove(item)

        if item:
            print(f'You have removed {item} from the room')
        else:
            print('There is no item by that name in the room')
