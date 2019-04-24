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
player = Player('Randy BoBandy', 'outside')
weapon = Weapon('Prison Shank', 10, 'good for stabbin')
personality_complex = Item('Existential Dread',
                           """so much angst and dread that it has manifested itself as a physical object""")

room['overlook'].add_item(weapon)
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

while response != "q" or response[0] != 'q':
    print(f'{player.name} is in {player.location} \n')
    print(f'{player.current_room.description}')

    response = input(
        "What would you like to do?\nChoose a cardinal direction (east/west/north/south)\n")

    response = response.split(' ')
    room = player.current_room

    if len(response) == 1:
        if response[0] == "north":
            player.change_room(room.n_to)
            print("You head to the north and find....\n")

        elif response[0] == "east":
            player.change_room(room.e_to)
            print("You head to the east and find...\n")

        elif response[0] == "west":
            player.change_room(room.w_to)
            print("You head to the west and find....\n")

        elif response[0] == "south":
            player.change_room(room.s_to)
            print("You go the only other direction left and find...\n")

        elif response[0] == "q":
            print("This game was too cool for you anyways! Bye Felicia\n")
            quit()

        else:
            print("Sorry that's not a valid direction \n")

    else:
        verb = response[0]
        item_name = response[1]

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
                f'You inspect the {item.name} and recognize it as the {item.about}')
            confirm = input(f'Would you like to take the {item.name}?\n')

            if confirm == 'yes':
                item.on_take(player)
                print(f"You took the {item.name}\n")

            else:
                print(
                    f"You left the {item.name} in the {player.location}\n")
        else:
            print("Sorry, that's not a valid command.\n")
