# http://www.codeskulptor.org/#user44_PkZdGlI89rqj6WS.py

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        string = ""
        for c in self.hand:
            string += c.get_suit() + c.get_rank() + " " 
        return "Hand contains " + string
        
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        count = 0
        ace = False
        for i in self.hand:
            count += int(VALUES.get(i.get_rank()))
            if i.get_rank() == "A":
                ace = True
        if ace and count <= 11:
            count += 10
        return count
   
    def draw(self, canvas, pos):
        for i in self.hand:
            rank = i.get_rank()
            suit = i.get_suit()
            hand=RANKS.index(rank)
            canvas.draw_image(card_images, [CARD_CENTER[0]+(hand)*CARD_SIZE[0],\
                                        CARD_CENTER[1]+SUITS.index(i.get_suit())*CARD_SIZE[1]],\
                          CARD_SIZE, pos, CARD_SIZE)        
            pos[0] += 75
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s,r))

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal_card(self):
        next_draw = self.deck.pop(0)
        return next_draw
    
    def __str__(self):
        string = ""
        for c in self.deck:
            string += c.get_suit() + c.get_rank() + " " 
        return "Deck contains " + string

#define event handlers for buttons
def deal():
    global in_play, players_hand, dealers_hand, deck, outcome, score
    outcome = ""
    dealers_hand = Hand()
    players_hand = Hand()
    deck = Deck()
    deck.shuffle()
    if in_play:
        score -= 1
    in_play = True
    for i in range(2):
        dealers_hand.add_card(deck.deal_card())
        players_hand.add_card(deck.deal_card())

    
def hit():
    global outcome, in_play, score
    if in_play:
        players_hand.add_card(deck.deal_card())
        print players_hand
    if players_hand.get_value() > 21:
        outcome = "you bust"
        score += -1
        in_play = False
        
def stand():
    global outcome, in_play, score
    if not in_play:
        return
    if players_hand.get_value() > 21:
        print outcome
    while dealers_hand.get_value() <= 17:
        dealers_hand.add_card(deck.deal_card())
    in_play = False
    if dealers_hand.get_value() > 21:
        outcome = "player wins"
        score += 1
    elif dealers_hand.get_value() >= players_hand.get_value():
        outcome = "dealer wins"
        score -= 1
    else:
        outcome = "player wins"
        score += 1

        

#" dealers total: " + str(dealers_hand.get_value()), " players total: " + str(players_hand.get_value())        
        
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("b l a c k j a c k", [92,65], 75,"White")
    canvas.draw_text("score: " + str(score), [445,100], 30,"Orange")   
    canvas.draw_text("dealer:", [50,180], 30,"Grey")
    canvas.draw_text("player:", [50,330], 30,"Grey")
    canvas.draw_text(outcome, [115,550], 75,"White")
    players_hand.draw(canvas,[100,400])
    dealers_hand.draw(canvas,[100,250])
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER,CARD_SIZE, [100,250], CARD_SIZE)
        canvas.draw_text('hit or stand?' ,(205,490), 20, 'Orange') 
    if not in_play:
        canvas.draw_text('dealers total: ' + str(dealers_hand.get_value()) + ',   players total: ' + str(players_hand.get_value()),(205,582), 20, 'Orange') 
        canvas.draw_text('new game?' ,(205,490), 20, 'Orange') 

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Navy")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric