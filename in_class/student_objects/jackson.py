class vegetable(object):
    def make_greener(self,amount):
                self.color = "really " + self.color
    def __init__(self):
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

vegetable = vegetable()
vegetable.owner = "HEB"
vegetable.make_greener(15)
print vegetable
