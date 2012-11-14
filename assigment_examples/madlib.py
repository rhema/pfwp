#Name: Rhema Linder
#Data: 10/??/2012
#Class: Programming Fundamentals With Python
#Assignment 4
#from www.classroomjr.com/mad-libs-worksheets/school-mad-libs-lunch-time/
text = """Make sure your lunch CONTAINER1 is filled with nutritious 
ADJECTIVE1 food.  Do not go to the ADJECTIVE2 food stand across the street 
from school.   The hamburgers they serve are fried in NOUN1 and are made of 
ANIMAL1 meat.   So take a sandwich made of VEGETABLE1 or VEGETABLE2 it's 
much healthier!  Drink COLOR1 milk instead of ADJECTIVE3 colas."""
adj = raw_input("Enter a CONTAINER")
text = text.replace("CONTAINER1",adj)
#add more like the above two lines until all capitalized words are replaced
print text