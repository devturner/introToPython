# http://www.codeskulptor.org/#user44_HnXDP0QIyLdLgUf.py

import simplegui


# template for "Stopwatch: The Game"

# define global variables
interval = 100 # 100 millisecs = .1 sec
passed_time = 0
tenths = 1
wins = 0
trys = 0
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tenths
    tenths = t % 10
    secs = int(t/10) % 10
    tens_mins = int(t/100) % 6
    mins = int(t/600)% 600 
    formated_time =  ("%d:%d%d:%d" % (mins, tens_mins, secs, tenths))
    return formated_time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    stopped = False
    timer.start()

def stop():
    global stopped, wins, trys, tenths
    if tenths == 0 and stopped == False:
        wins += 1
        trys += 1
        stopped = True
        timer.stop()
    elif stopped == False:
        trys += 1
        stopped = True
        timer.stop()
    
def restart():
    global passed_time, wins, trys, stopped
    passed_time = 0
    wins = 0
    trys = 0
    stopped = True
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global passed_time
    passed_time += 1

# define draw handler
def draw(canvas):
    global passed_time
    canvas.draw_text(format(passed_time), (110,125), 75, "Red")
    canvas.draw_text(str(wins) + "/" + str(trys), (300, 40), 36, "Yellow")

# create frame
frame = simplegui.create_frame("Converter", 400, 200)
frame.add_button("Start", start, 75)                        
frame.add_button("Stop", stop, 75)
frame.add_button("Reset", restart, 75)
# register event handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(interval, timer_handler)

# start frame
frame.start()

