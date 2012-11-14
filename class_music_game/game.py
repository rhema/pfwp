import random

file = open("lastfm_unique_tags.txt")
lines = file.readlines()

tag_dictionary = {}

for line in lines:
#	print line
	tag,number = line.split("\t")
	number = float(number)
#	print tag
#	print number
	tag_dictionary[tag] = number


keys = tag_dictionary.keys()

def dont_stop():
	
	random_word1 = keys[int(random.random()*len(keys))]
	random_word2 = keys[int(random.random()*len(keys))]
	
	print "Is",random_word1,"more popular than",random_word2,"? (please type 'yes', 'no', or stop)"
	word = raw_input("")
	
	if tag_dictionary[random_word1] > tag_dictionary[random_word1]:
	    print "It is!"
	    if word == "yes":
	        print "right!"
	    else:
	        print "wrong!"
	else:
	    print "It is not!"
	    if word == "no":
	        print "right!"
	    else:
	        print "wrong!"
	if word == "stop":
		return False
	return True
	
while dont_stop():
	print "Try again"