import random

zombies = 100
hero = 1
armor = 50
shotgun_rounds = 10
progress_start = 0
progress_end = 100
progress = progress_start

while hero > 0 and zombies > 0 and progress < progress_end:
    print zombies,hero,armor,shotgun_rounds,progress
    progress = 10 + progress
    choice = input("What do you want to do (1->Nothing?) (2->shoot)")
    if choice == 1:
        print "You did nothing"
    if choice == 2:
        shotgun_rounds -= 1
        number_shot = int(random.random()*10)
        zombies -= number_shot
        print "You just shot",number_shot,"zombies!"
        print "there are",zombies,"zombies left."
#TBD: add, you won, lost, messages.  Make it possible to win and lose.