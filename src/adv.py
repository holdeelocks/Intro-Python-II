from room import Room

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
while response not in directions:
    # print(f'{Player} is in room {player.current_room.name} \n')
    # print(f'{player.current_room.description}')
    response = input(
        "What would you like to do?\nChoose a cardinal direction (east/west/north/south)\n")
    response = response.split(' ')
    if len(response) == 1:
        if response[0] == "north":
            print("You head to the north and find....\n")
        elif response[0] == "east":
            print("You head to the east and find...\n")
        elif response[0] == "west":
            print("You head to the north and find....\n")
        elif response[0] == "south":
            print("You go the only other direction left and find...\n")
        elif response[0] == "q":
            print("This game was too cool for you anyways!. Bye Felicia")
            quit()
    else:
        verb = response[0]
        item = response[1]
        if verb == 'drop':
            confirm = input("Are you sure you'd like to drop that item?")
            if confirm == 'yes':
                print('You dropped the item')
            else:
                print('You did not drop the item')
        elif verb == 'take':
            confirm = input('Would you like to take that item?')
            if confirm == 'yes':
                print("You took the item")
            else:
                print("You left the item in the room")
        else:
            print("I didn't understand that.\n")
