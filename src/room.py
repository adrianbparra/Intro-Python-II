# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self,name,desc,is_light,items):
        self.name = name
        self.desc = desc
        self.items: List[Item] = items
        self.is_light : bool = is_light

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        return self.desc

    def print_items(self):
        if len(self.items) > 0:
            print(f"Wow look what is {self.name}:")
            print("You want to take one?")
            for item in self.items:
                print(f"{item}")
        else:
            print("Nothing found " + self.name)

    def remove_item(self,item_index):
        item = self.items.pop(item_index)
        
        item.on_take()

        return item
    
    def add_item(self,item):

        self.items.append(item)

