# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self,name,desc,items):
        self.name = name
        self.desc = desc
        self.items: List[Item] = items

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        return self.desc

    def print_items(self):
        print(f"Wow look whats {self.name}:")
        print("You want to take one?")
        for item in self.items:
            print(f"{item}")


    def remove_item(self,item_index):
        item = self.items.pop(item_index)
        item.on_take()

        return item
        pass