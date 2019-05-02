from room import Room
from player import Player
from item import Item, Weapon


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Randy BoBandy', room['outside'])
weapon = Weapon(10, "prison shank", "good for stabbin")
# weapon.name = "Prison Shank"
# weapon.about = "good for stabbin"
personality_complex = Item('Existential Dread',
                           """so much angst and dread that it has manifested itself as a physical object""")

room['overlook'].add_item(weapon)
room['foyer'].add_item(weapon)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ["east", "west", "north", "south"]
response = ""

while True:
    print(f'{player.name} is in {player.current_room.name} \n')
    print(f'{player.current_room.description}')
    room = player.current_room
    exits = room.get_exits()
    print('You notice there are exits to the...')
    for path in exits:
        print(f"{path}\t")

    if len(room.items) > 0:
        print('\nYou notice these items in the room:')
        for item in room.items:
            print(f"{item.name}, {item.about}\n")
    response = input(
        "What would you like to do?\n--> ")

    response = response.split(' ')

    if response[0] in directions:
        player.change_room(response[0])
        print(f"You head to the {response[0]} and find....\n")

    elif response[0] == 'i' or response[0] == 'inventory':
        if len(player.inventory) > 0:
            print('You have the following items:')
            for item in player.inventory:
                print(f"{item.name}, {item.about}\n")
        else:
            print(f"Sorry {player.name}, your inventory is empty.\n\n\n\n\n")
    elif response[0] == 'q':
        print(
            f"\n\n\n\n\nFine {player.name}, we didn't want you to play anyways")
        break
    elif len(response) > 1:
        verb = response[0]
        item_name = ' '.join(response[1:])

        if verb == 'drop':
            item = player.get_item(item_name)
            confirm = input(
                f"Are you sure you'd like to drop the {item.name}?\n")

            if confirm == 'yes':
                item.on_drop(player)
                print(f'You dropped the {item.name}\n')

            else:
                print(f'You did not drop the {item.name}\n')

        elif verb == 'take' or verb == 'get':
            item = room.get_item(item_name)

            print(
                f'You inspect the {item.name} and recognize it as {item.about}')
            confirm = input(f'Would you like to take the {item.name}?\n')

            if confirm == 'yes':
                item.on_take(player)
                print(f"You took the {item.name}\n")
            elif confirm == 'q':
                print(
                    f"Fine {player.name}, we didn't want you to play anyways")
                break
        else:
            print(
                f"You left the {item.name} in the {player.location}\n")
    else:
        print("Sorry, that's not a valid command.\n")
