# http://www.codeskulptor.org/#user44_o2ErNzTnLAjpHlW.py

import simplegui
import random

deck = []
exposed = [False]*16
state = 0
card1 = 0
card2 = 0
back1 = 0
back2 = 0
score = 0
i = 0

def new_game():
    global exposed, state, deck, score, back1, back2, card1, card2
    deck1 = range(8)
    deck2 = range(8)
    deck = deck1 + deck2
    random.shuffle(deck)
    exposed = [False]*16
    state = 0
    card1 = 0
    card2 = 0
    back1 = 0
    back2 = 0
    score = 0
    i = 0
    
def mouseclick(pos):
    global exposed, state, card1, card2, i, back1, back2, score
    i = pos[0] / 50
    if not exposed[i]: 
        if state == 0:
            exposed[i] = True
            card1 = deck[i]
            back1 = i
            state = 1
        elif state == 1: 
            exposed[i] = True
            card2 = deck[i]
            back2 = i
            state = 2
            score += 1
            label.set_text("turns: " + str(score))
        else:
            state = 1
            if int(card1) == int(card2):
                exposed[back1] = True
                exposed[back2] = True
                exposed[i] = True
                back1 = i
                card1 = deck[i]
            else:
                exposed[back1] = False
                exposed[back2] = False
                exposed[i] = True
                back1 = i
                card1 = deck[i]
    else: 
        pass
    
def draw(canvas):
    global exposed, deck
    frontside_space = 0
    backside_space = 0
    for i in deck:
        canvas.draw_text(str(i), (10 + frontside_space, 69), 60, "Fuchsia")
        frontside_space += 50
    for i in range(len(exposed)):
        if exposed[i]:
            backside_space += 50
        else:
            canvas.draw_line([25+backside_space, 2], (25+backside_space, 98), 48, 'Green')
            backside_space += 50

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
