# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self,name, current_room,items):
        self.name = name
        self.current_room = current_room
        self.items : List[items] = items

    def location(self):
        print(f"You are {self.current_room.name} \n{self.current_room.desc}")

    def itemsonplayer(self):
        # shows how many items and lists them.
        print(f"You have {len(self.items)} items:")
        for item in self.items:
            print(f"{item}")

    def additem(self):
        # adds items to item from current room
        pass

    def move(self,direction):
        # direction n,s,e,w
        if direction == "n":
            if (self.current_room.n_to):
                self.current_room = self.current_room.n_to
                self.location()

            else:
                print("Wrong way bud!")
        elif direction == "e":
            if (self.current_room.e_to):
                self.current_room = self.current_room.e_to
                self.location()

            else:
                print("Can't go that way!")
        elif direction == "s":
            if(self.current_room.s_to):
                self.current_room = self.current_room.s_to
                self.location()

            else:
                print("Try another way!")
                
        elif direction == "w":
            if(self.current_room.w_to):
                self.current_room = self.current_room.w_to
                self.location()

            else:
                print("That way is not possible.")