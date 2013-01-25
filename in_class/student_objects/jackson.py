class Food(object):
    def __init__(self):
        self.salty = 0
        self.spicy = 0
        self.sweet = 0
        self.bitter = 0
        self.savory = 0
        self.raw = True
        self.poisoned = False
    
    def human_edible(self):
        if self.poisoned:
            return False
        return True

    def cook(self):
        self.raw = False

    def poison(self):
        self.poisoned = True
        self.bitter = 1

class Meat(Food):
    def __init__(self):
        super(Meat, self).__init__()
        self.savory = .4
    
    def human_edible(self):
        if self.raw == True or Food.human_edible(self) == False:
            return False
        return True

class Vegetable(Food):
    def make_greener(self,amount):
            self.color = "really " + self.color
    def __init__(self):
        super(Vegetable, self).__init__()
        self.owner = "HEB"
        self.weight = 1
        self.size = 150
        self.crunchy = 7
        self.color = "green"

    def __str__(self):
        ret_string = self.owner+","+str(self.weight)+","+str(self.size)+","+str(self.crunchy)+","+self.color
        return ret_string

def classless_function(num):
        print num*2

vegetable = Vegetable()
vegetable.owner = "HEB"
vegetable.make_greener(15)
print "I can eat the vegitable?",vegetable.human_edible()
print "try poison"
vegetable.poison()
print "I can eat the vegitable?",vegetable.human_edible()

patty = Meat()

print "I can eat the meat?",patty.human_edible()
print "try cook"
patty.cook()
print "I can eat the meat?",patty.human_edible()
print "try poison"
patty.poison()
print "I can eat the meat?",patty.human_edible()
