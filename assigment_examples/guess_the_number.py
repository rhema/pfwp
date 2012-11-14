#Name: Rhema Linder
#Data: 10/??/2012
#Class: Programming Fundamentals With Python
#Assignment 3
import random
number = 1+int(random.random()*1000)
guess = -1
while guess != number:
    guess = input("Guess a number between 1 and 1000:")
    if guess == number:
        print "You picked the right number!"
    else:
        print "Nope!"
#TBD: give guess higher, or guess lower hints