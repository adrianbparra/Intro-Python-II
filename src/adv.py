from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside The Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("On The Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("On The Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("On A Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("In A Treasure Chamber", """You've found the long-lost treasure
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
print("\n")
print("Welcome to Adrian's Adventure!")

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player(room["outside"])

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
while True:
    print(newPlayer)
    print("\n")
    
    print("Type N,E,S,W to travel within my mansion or type q to quit:")
    newroom = input("Where would you like to go? ")


    if newroom == "n":
        if newPlayer.current_room.n_to:
            newPlayer.current_room = newPlayer.current_room.n_to
        else:
            print("Wrong way bud!")
        pass
    elif newroom == "e":
        newPlayer.current_room = newPlayer.current_room.e_to

        pass
    elif newroom == "s":
        pass
    elif newroom == "w":
        pass
    else:
        print("Try again!")
    
    