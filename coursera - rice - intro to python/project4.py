# http://www.codeskulptor.org/#user44_YtJK3cqBznnMHjQ.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400      
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
   
    ball_pos = [WIDTH/2, HEIGHT/2]
   
    horizontal_vel = random.randrange(133, 233)/55
    vertical_vel = random.randrange(55, 188)/55
   
    if direction == LEFT:  # upper and left
        ball_vel = [-horizontal_vel,-vertical_vel]
    elif direction == RIGHT:   # upper and right
        ball_vel = [horizontal_vel, -vertical_vel]
       
# define event handlers
def new_game():
    global pad1_pos, pad2_pos, pad1_vel, pad2_vel  # these are numbers
    pad1_pos = [HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]
    pad2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2 - HALF_PAD_HEIGHT]         
    pad1_vel = 0
    pad2_vel = 0
   
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
   
    spawn_ball(LEFT)
   
def draw(canvas):
    global score1, score2, pad1_pos, pad2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "Green")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Red")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Red")
      
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
   
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS-1, 1, "White","White")
   
    # update paddle's vertical position, keep paddle on the screen
    pad1_pos[1] += pad1_vel
    if pad1_pos[1] < 0:
        pad1_pos[1] = 0
    elif pad1_pos[1] > HEIGHT - PAD_HEIGHT - 3:
        pad1_pos[1] = HEIGHT - PAD_HEIGHT - 3
       
    pad2_pos[1] += pad2_vel
    if pad2_pos[1] < 0:
        pad2_pos[1] = 0
    elif pad2_pos[1] > HEIGHT - PAD_HEIGHT - 3:
        pad2_pos[1] = HEIGHT - PAD_HEIGHT - 3   
       
    # draw paddles
    canvas.draw_line(pad1_pos,[pad1_pos[0], pad1_pos[1]+PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line(pad2_pos,[pad2_pos[0], pad2_pos[1]+PAD_HEIGHT], PAD_WIDTH, "White")
   
    # determine whether paddle and ball collide 
    if (ball_pos[1] - BALL_RADIUS <= 0):
        ball_vel[1] = -ball_vel[1]
    else:
        if ball_pos[1] + BALL_RADIUS >= HEIGHT - 1: 
            ball_vel[1] = -ball_vel[1]
           
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH - 1: # touch left
        if ball_pos[1] >= pad1_pos[1] and ball_pos[1] <= pad1_pos[1]+PAD_HEIGHT: # strike paddle
            ball_vel[0] = -ball_vel[0]*1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
    else:
        if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH - 1: # touch right
            if ball_pos[1] >= pad2_pos[1] and ball_pos[1] <= pad2_pos[1]+PAD_HEIGHT: # strike paddle
                ball_vel[0] = -ball_vel[0]*1.1
            else:
                spawn_ball(LEFT)
                score1 += 1
               
    # draw scores
    canvas.draw_text(str(score1), [WIDTH/4, HEIGHT/5], 44, "Yellow")
    canvas.draw_text(str(score2), [WIDTH*3/4, HEIGHT/5], 44, "Yellow")
   
def keydown(key):
    global pad1_vel, pad2_vel
    if key == simplegui.KEY_MAP['w']:
        pad1_vel = -1
    elif key == simplegui.KEY_MAP['s']:
        pad1_vel = 1
    elif key == simplegui.KEY_MAP["up"]:
        pad2_vel = -1
    elif key == simplegui.KEY_MAP["down"]:
        pad2_vel = 1

def keyup(key):
    global pad1_vel, pad2_vel

    if key == simplegui.KEY_MAP['w']:
        pad1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        pad1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        pad2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        pad2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)

# start frame
new_game()
frame.start()


# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400      
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
SIDE = LEFT

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]    # position the ball at the centre of the canvas
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60, -(random.randrange(60, 180) /60)]
    else:
        ball_vel = [-(random.randrange(120, 240) / 60), -(random.randrange(60, 180) / 60)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global SIDE #this is a boolean
    paddle1_pos, paddle2_pos = (HEIGHT - PAD_HEIGHT)/2, (HEIGHT - PAD_HEIGHT)/2
    paddle1_vel = paddle2_vel = 0
    score1, score2 = 0, 0
    SIDE = not SIDE
    spawn_ball(SIDE)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
       
    # update ball
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score2 += 1
    if ball_pos[0] >= (WIDTH - BALL_RADIUS - PAD_WIDTH):
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos+PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
        else:
            spawn_ball(LEFT)
            score1 += 1
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
           
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 0.1, "White", "White")
   
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel
   
    # draw paddles
    canvas.draw_line([PAD_WIDTH / 2, paddle1_pos],[PAD_WIDTH / 2, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH / 2, paddle2_pos],[WIDTH- PAD_WIDTH / 2, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "White")
   
    # draw scores
    canvas.draw_text(str(score1), (185, 40), 40, "White")
    canvas.draw_text(str(score2), (400, 40), 40, "White")
       
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 3
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -vel  
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -vel
  
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0  
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
       
def game_restart():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", game_restart, 100)

# start frame
new_game()
frame.start()