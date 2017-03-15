# Swamp monster game.
# version 1.0

from sys import exit

print "-----------------------"
print "|  Swamp Monster!     |"
print "|                     |"
print "|    by JSirikool     |"
print "-----------------------"

def swamp_monster():
    print "A giant green swamp monster rises from the waters!"
    print "It stares at you with big black eyes."
    print "It raises it's slimey hands and moves towards you..."
    print "What do you do?"
    monster_defeated = False

    while True:
        choice = raw_input ("'jump off boat' or 'attack the monster?' ")

        if choice == "jump off boat" or choice == "jump":
            dead("The swamp monster catches you and chokes you to death!")
        elif choice == "attack the monster" or choice == 'attack' and not monster_defeated:
            print "The monster is surprised you attacked and backs into the swamp."
            monster_defeated = True
            land()
        else:
            print "You only have two choices."

def land():
    print "Your boat drifts away and the fog finally clears."
    print "You see some land ahead."
    print 'What do you?'
    choice = raw_input("'Get off the boat' or 'keep going' ")

    if choice == "get off":
        print "You see a cave up ahead"
        exit(0)
    elif choice == "keep going":
        dead("The swamp monster returns and drags you into the swamp.")







def dead(why):
    print why, "Good job! You're dead!"
    exit(1)

def start():
    print """You're in the deep South. \nYou're on a row boat in the sawmp. \
    \nIt's foggy. You hear a splash and seomthing is moving towards you. \
    \nWhat do you do you? \npaddle away, ask questions later. \
    \nWait, see what it is."""

    choice = raw_input("> ")

    if choice == "paddle away" or choice == "paddle":
        swamp_monster()
    else:
        dead("You did nothing!")

start()
