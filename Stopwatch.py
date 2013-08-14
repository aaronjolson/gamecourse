# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.
#try to stop the clock on exact 1 second intervals

import simplegui
import math

#global variables
message = '0:00.0'
points = '0/0'
time = 0

x = 0
y = 0

A = 0
B = 0
C = 0

# Handler for start button click
def start():
    timer.start()

#Handler for stop button   
def stop():
    score()
    timer.stop()
    

            
#Handler for restart button
def restart():
    global time
    global message
    global points
    global x
    global y
    
    time = 0
    x = 0
    y=0
    message = '0:00.0'
    points = '0/0'
    
    stop()
    
    

#arithmetic for display    
def formatt(time):
    global A
    global B
    global C
    
    A = time // 600
    B = (time // 10) % 60
    C = time % 10

# timer handler
def timer_handler():
    global message,time
    global C
    time +=1
    formatt(time)
    message = str(A)+":"+ str(B) +'.'+str(C)
    if B < 10:
            message = message = str(A)+":"+'0'+ str(B)+'.'+ str(C)

#Handler for Scoring
def score():
    global C
    global x
    global y
    global points
    
    if timer.is_running() and C == 0:
        x += 1
        y += 1
        
    elif timer.is_running() and C != 0:
        x += 1
        
    points = str(x) + '/' + str(y)
            
#bring in a picture
image = simplegui.load_image("http://info.hoganassessments.com/Portals/153377/images/SpeedCoaching96-252x300.png")

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_image(image, (125,120), (240,240), (250,250), (500,500))
    canvas.draw_text(message, [170,370], 70, "Red")
    canvas.draw_text(points, [380,60], 70, "Red")
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Timer", 500, 500)
frame.set_draw_handler(draw)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Restart", restart)
timer = simplegui.create_timer(100, timer_handler)


# Start the frame animation
frame.start()
