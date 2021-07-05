class Item():
    def __init__(self,name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name + " = " + self.description

    def __repr__(self):
        return self.name + " : " + self.description

    def on_take(self):
        print("You have picked up " + self.name) 

    def on_drop(self):
        print("You dropped "+ self.name)



class Key(Item):
    def __init__(self,name,description,key_id):
        super().__init__(name,description)
        self.key_id = key_id

class LightSource(Item):
    def __init__(self,name,description):
        super().__init__(name,description)


    def on_drop(self):
        print("It's not wise to drop your source of light!")



class Chest(Item):
    def __init__(self, name, description, unlocked, item: None, chest_id):
        super().__init__(name, description)
        self.unlocked = unlocked
        self.item = item
        self.chest_id = chest_id

    def on_open(self):
        # check if unlocked
        print("You have opened a " + self.name)
        print("It had a " + self.item.name)
