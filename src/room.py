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
        print(f"Wow look what items are {self.name}:")
        print("You want to take one?")
        for item in self.items:
            print(f"{item}")