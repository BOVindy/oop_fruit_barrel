# build a fruit stand that has a barrel for fruit and fruits have:
# a name, a price, 
# you should be able to get the total cost of the barrel given the number of fruits in in it
# and you should be able to get the fruit cost
# a barrel can only hold one fuit type

# fruit obj

# barrel obj
"""
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Barrel:
    def __init__(self):
        self.fruit_count = 0
        self.fruit_type = None

    def sum_total(self):
        return self.fruit_count * self.fruit_type.price
"""
"""
### structuring it this way is less readable and performs more operations than needed
    def add_fruit(self, fruit):
        if self.fruit_type == fruit.name or self.fruit_type == None:
            self.fruit_type = fruit
            self.fruit_count += 1
        else:
            return "invalid barrel for that type of fruit"
"""
"""
    def add_fruit(self, fruit):
        if self.fruit_type == fruit.name
            self.fruit_count += 1
        elif self.fruit_type == None:
            self.fruit_type = fruit
            self.fruit_count += 1
        else:
            return "invalid barrel for that type of fruit"

apple = Fruit("apple", 1.2)

apple_barrel = Barrel()

apple_barrel.add_fruit(apple)
print(apple_barrel.sum_total())
"""
    

###### create a menu that adds full crud functionallity
# add to a barrel,
# get type of fruit in barrel
# remove a quant of fruit from barrel
# reset the barrel (emptying it and setting type to none)
# exit


# ALSO make the needed barrel methods
# DUE: start of class tomorrow 


class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Barrel:
    def __init__(self):
        self.fruit_count = 0
        self.fruit_type = None

    def sum_total(self):
        return self.fruit_count * self.fruit_type.price

    def add_fruit(self, fruit):
        if self.fruit_type == fruit:
            self.fruit_count += 1
        elif self.fruit_type == None:
            self.fruit_type = fruit
            self.fruit_count += 1
        else:
            return "invalid barrel for that type of fruit"
"""
class Menu:
    def __init__(self):
        self.notes = []

    def fruit_type(self, name):
        self.name = name
        print(self.name)



    def _find_note(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def update_message(self, note_id, message):
        note = self._find_note(note_id)
        if note:
            note.message = message
            return True
        return False
"""

class Menu:
    def __init__(self):
        self.fruit_count = 0
        self.fruit_type = None

    def add_fruit(self, fruit):
        if self.fruit_type == fruit:
            self.fruit_count += 1
        elif self.fruit_type == None:
            self.fruit_type = fruit
            self.fruit_count += 1
        else:
            return "invalid barrel for that type of fruit"

    def get_type(self, fruit):
        get_type = self.fruit_type

    def sum_total(self):
        return self.fruit_count * self.fruit_type.price

    def remove_fruit(self, fruit):
        if self.fruit_type == fruit:
            self.fruit_count -= input(int("what quantity of fruit would you like to remove? \n> "))
        else:
            return "invalid barrel for that type of fruit"

    def empty_barrel(self):
        if self.fruit_type != None:
            self.fruit_type == None
            self.fruit_count == None
        else:
            print("your barrel is already empty")

    def exit(self):
        exit()




funt = Menu()
funt.add_fruit("apple")
print(funt.fruit_count)