class Item:
    def __init__(self, name, damage, about):
        self.name = name
        self.damage = damage
        self.about = about

    def on_take(self, player):
        room_items = player.current_room.items
        valid_item = room_items.remove(self)

        if valid_item:
            player.inventory.append(self)
            print(f'{player} has put {self.name} in their inventory')
        else:
            print(
                f'Sorry {player} you cannot pick up an item that is not here')

    def on_drop(self, player):
        valid_item = player.inventory.remove(self)

        if valid_item:
            player.current_room.add_item(self)
            print(f"{player} has dropped {self.name} from their inventory")
        else:
            print(f"{player}'s inventory doesn't have an item by that name")
