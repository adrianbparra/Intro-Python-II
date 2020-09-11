from room import Room
from player import Player
from item import Item

# Declare all the rooms

Item("","")

room = {
    'outside':  Room("Outside The Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("silver sword", "With a sharp blade this can cut anything"),Item("lamp","Lights up the most dark places")]
                     ),

    'foyer':    Room("on the Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    [Item("rusty sword","It is a little rusty but should do some damage"),Item("stick","It can probably be ligthed up") ]
                    ),

    'overlook': Room("on the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[Item("Rock","Well you can throw this to someone")]),

    'narrow':   Room("on a Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[Item("bone","Huh! Who can this belong to"), Item("bronze sword", "Wow. well seems like this didn't help much.")]),

    'treasure': Room("in a Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[Item("gold nugget","So maybe one piece of gold was left behind"),Item("key", "What can this unlock now?")]),
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
name = input("Enter your name: ")
print("\n")

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player(name,room["outside"],[])

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
print(f"Welcome {newPlayer.name} to my Adventure!")
print("Type N,E,S,W to travel within my mansion or type q to quit.\n")

newPlayer.location()
while True:
    
    # action is a list
    action = input("What would you like to do? ").split( )

    for i in range(len(action)):
        action[i] = action[i].lower()
 
    print("\n")
    
    if len(action) == 1:

        if action[0] == "q":
            print(f"Is {newPlayer.name} to scared?!")
            break

        elif action[0] == "look":
            newPlayer.current_room.print_items()


        # show items
        elif action[0] in ["i", "inventory"]:
            newPlayer.items_on_player()

        elif action[0] in ["n","s","w","e"]:
            newPlayer.move(action[0])
            pass
        else:
            print(f"You can not {action[0]}")
    
    if len(action) >= 2:

        if action[0] in ["get","take"]:
            item = " ".join(action[1:]) 
      
            newPlayer.add_item(item)

            pass

        elif action[0] in ["drop"]:
            item = " ".join(action[1:]) 
            
            newPlayer.drop_item(item)

        else:
        # if no action[0] then say
            print("You can not", *action, sep=" ")
        pass