# Write a class to hold player information, e.g. what room they are in
# currently.
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

            print(item)

            self.items.append(item)

            pass
        except ValueError:
            print("There was no " + item_searched + " " + self.current_room.name)
            pass

        # print(index)
        # if item_searched in [itm.name for itm in self.current_room.items]:
        #     # adds items to item from current room

        #     pass
        # else:
        #     print(f"{item_searched} is no where to be found")
        # pass

    def drop_item(self):
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