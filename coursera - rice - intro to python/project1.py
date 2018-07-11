# http://www.codeskulptor.org/#user44_TY61dUHanK_1.py

import random

def name_to_number(name):
    if name == "rock":
        name = 0
    elif name == "Spock":
         name = 1         
    elif name == "paper":
         name = 2         
    elif name == "lizard":
         name = 3         
    elif name == "scissors":
         name = 4         
    else:
        name = "Not playable name"
    return name

def number_to_name(number):
    if number == 0:
        number = "rock"
    elif number == 1:
         number = "Spock"         
    elif number == 2:
         number = "paper"        
    elif number == 3:
         number = "lizard"        
    elif number == 4:
         number = "scissors"         
    else:
        number = "Not playable number"
    return number
   
def rpsls(player_choice):
    print
    print "Player chose: " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer plays: " + comp_choice
    digit = (player_number - comp_number) % 5
    if digit == 0:
        print "Player and computer tie!"
    elif digit <= 2:
        print "Player wins"
    elif digit >= 3:
        print "Computer wins"
    else:
        print "Somthing has gone terribly wrong!!!"


# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")