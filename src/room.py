# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def get_exits(self):
        directions = []
        if self.n_to is not None:
            directions.append('north')
        if self.e_to is not None:
            directions.append('east')
        if self.w_to is not None:
            directions.append('west')
        if self.s_to is not None:
            directions.append('south')

        return directions

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
