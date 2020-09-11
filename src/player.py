# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource

class Player():
    def __init__(self,name, current_room,items):
        self.name = name
        self.current_room = current_room
        self.items : List[items] = items

    def location(self):
        print(f"You are {self.current_room.name} \n{self.current_room.desc}")

    def items_on_player(self):
        # shows how many items and lists them.
        print(f"You have {len(self.items)} items:")
        for item in self.items:
            print(f"{item}")

    def add_item(self,item_searched):
        # checks if item in current room
        try:
            index = [itm.name for itm in self.current_room.items].index(item_searched)

            item = self.current_room.remove_item(index)

            self.items.append(item)

        except ValueError:
            print("There was no " + item_searched + " " + self.current_room.name)

    def drop_item(self,item_searched):
        
        try:
            index = [itm.name for itm in self.items].index(item_searched)

            item = self.items.pop(index)

            item.on_drop()

            self.current_room.add_item(item)

        except ValueError:
            print("You dont have "+ item_searched + " to drop.")

    def has_light(self):
        if any(isinstance(item, LightSource) for item in self.items) or any(isinstance(item, LightSource) for item in self.current_room.items) or self.current_room.is_light == True:
            return True
        else:
            return False

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