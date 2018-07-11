# http://www.codeskulptor.org/#user44_tMdJIACN0Ma2yI6.py

import simplegui
import random


secret_number_1000 = None


# helper function to start and restart the game
def new_game():
    global secret_number, secret_number_1000, total_turns, turns
    turns = 0
    print
    if secret_number_1000:
        secret_number = secret_number_1000
        total_turns = 10
        print "New game. Range is (0, 1000)"
        print "Number of remaining guesses is 10"
       
    else:
        secret_number = random.randrange(0,100)
        total_turns = 7
        print "New game. Range is (0, 100)"
        print "Number of remaining guesses is 7"

# define event handlers for control panel
def range100():
    reset_numbers()
    new_game()


def range1000():
    global secret_number_1000
    reset_numbers()
    secret_number_1000 = random.randrange(0,1000)
    new_game()
   
def reset_numbers():
    global secret_number_1000, secret_number
    secret_number = None
    secret_number_1000 = None   
   
   
def input_guess(guess):
    global turns
    guess_int = int(guess)   
    if guess_int == secret_number:
        turns += 1
        print "You won!!! The number was:", guess_int
        print "Starting over"
        if secret_number_1000:
            range1000()
        else:
            new_game()
    elif guess_int < secret_number:
        turns += 1
        print "Guess was", guess_int
        print "Guess higher, turns remaining:", total_turns - turns
    else:
        turns += 1
        print "Guess was", guess_int
        print "Guess lower, turns remaining:", total_turns - turns
    if total_turns - turns == 0 :
        print "You lost, starting a new game, number was", secret_number
        if secret_number_1000:
            range1000()
        else:
            new_game()
       
   
# create frame
frame = simplegui.create_frame("Home", 300, 200)
frame.add_input('Guess a number', input_guess, 75)
frame.add_label("Start a new game")
frame.add_button("Range is (0,100)", range100, 100)
frame.add_button("Range is (0,1000)", range1000, 100)

# call new_game
new_game()