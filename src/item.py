class Item:
    def __init__(self, name, about):
        self.name = name
        self.about = about

    def on_take(self, player):
        room_items = player.current_room.items
        valid_item = [i for i in room_items if i.name == self.name]

        if valid_item:
            player.current_room.items = list(
                filter(lambda i: i.name != self.name, room_items))
            player.inventory.append(self)
            print(f'{player.name} has put {self.name} in their inventory')
        else:
            print(
                f'Sorry {player.name} you cannot pick up an item that is not here')

    def on_drop(self, player):
        items = player.inventory
        valid_item = [i for i in items if i.name == self.name]

        if valid_item:
            player.current_room.add_item(self)
            player.inventory = list(
                filter(lambda i: i.name != self.name, items))
            print(f"{player.name} has dropped {self.name} from their inventory")
        else:
            print(f"{player.name}'s inventory doesn't have an item by that name")


class Weapon(Item):
    def __init__(self, damage, name, about):
        self.damage = damage
        super().__init__(name, about)
