from room import Room
from player import Player

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

curr_player = Player('GhostWolf', 'outside')

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

# check for valid user input


# Declare current room 
curr_room = room[curr_player.curr_room]

# Get key from room dictionary
def get_key(val):
    for key, value in room.items():
        if val == value.name:
            return key

# Helper to print out room name and room desc
def room_details():
    print(f'\n{curr_player.name} is currently in the {curr_room.name}\n')
    print(f'Room Description: {curr_room.desc}\n')

# Check for valid input and move player into the apprpriate room if able to
# try/except block used in accordance with
# easier to ask for forgiveness than permission(EAFP) guidelines
def check_input(choice):
    global curr_room
    if choice == "w":
        try:
            print(f'\n{curr_player.name} headed west towards the {curr_room.w_to.name}')
            curr_player.set_curr_room(get_key(curr_room.w_to.name))
            curr_room = room[curr_player.curr_room]
        except AttributeError:
            print(f'\n{curr_player.name} took a quick turn to the west and ran into a dead end!!')
    elif choice == "n":
        try:
            print(f'\n{curr_player.name} headed north towards the {curr_room.n_to.name}')
            curr_player.set_curr_room(get_key(curr_room.n_to.name))
            curr_room = room[curr_player.curr_room]
        except AttributeError:
            print(f'\n{curr_player.name} took a quick turn to the north and ran into a dead end!!')
    elif choice == "e":
        try:
            print(f'\n{curr_player.name} headed east towards the {curr_room.e_to.name}')
            curr_player.set_curr_room(get_key(curr_room.e_to.name))
            curr_room = room[curr_player.curr_room]
        except AttributeError:
            print(f'\n{curr_player.name} took a quick turn to the east and ran into a dead end!!')
    elif choice == "s":
        try:
            print(f'\n{curr_player.name} headed south towards the {curr_room.s_to.name}')
            curr_player.set_curr_room(get_key(curr_room.s_to.name))
            curr_room = room[curr_player.curr_room]
        except AttributeError:
            print(f'\n{curr_player.name} took a quick turn to the south and ran into a dead end!!')
    else:
        print('\nUh Oh!! Looks like your player got tired and decided to take a nap!')


room_details()
selection = input('Please choose a direction (N, S, E, W): ').lower()

while(selection != 'q'):
    check_input(selection)
    room_details()
    selection = input('Please choose a direction (N, S, E, W): ').lower()
    

