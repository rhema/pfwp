class Chair(object):
	def make_heavier(self,amount):
		self.weight += amount

	def __init__(self):
		self.owner = "manufacturer"
		self.weight = 15
		self.height = 50
		self.legs = 4
		self.seat = "hard"
	
	def __str__(self):
		ret_string = self.owner+","+str(self.weight)+","+str(self.height)+","+str(self.legs)+","+self.seat
		return ret_string

def classless_function(num):
	print num*2

rhemas_chair = Chair()
rhemas_chair.owner = "rhema"
rhemas_chair.make_heavier(15)
print rhemas_chair 

light_chair = Chair()
light_chair.make_heavier(rhemas_chair.weight*-1)
print light_chair