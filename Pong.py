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

paddle1_pos = [230, 150]
pad_vel = 0

paddle2_pos = [230, 150]
pad2_vel = 0

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-40 / 40,  -100 / 60]

pt1 = 0
pt2 = 0
score = str(pt1)+'/'+str(pt2)

#spawn ball
def ball_initr():
    global ball_pos, ball_vel
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [-40 / 40,  -100/60]
    
def ball_initl():
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [40 / 40,  -100 / 60]

#Event handlers
#Handler for restart button
def restart():
    global paddle1_pos, paddle2_pos, pad_vel, pad2_vel, pt1, pt2, score
   
    #return paddles to original positions
    paddle1_pos = [230, 150]
    pad_vel = 0
    paddle2_pos = [230, 150]
    pad2_vel = 0
    
    #return score to zeros
    pt1 = 0
    pt2 = 0
    score = str(pt1)+'/'+str(pt2)
    
    ball_initr()

#scoring functions
def p1score():
    global pt1, score , pt2
    pt1 += 1
    score = str(pt1)+'/'+str(pt2)
def p2score():
    global pt1, score , pt2
    pt2 += 1
    score = str(pt1)+'/'+str(pt2)
    
def draw(canvas):
    global score, paddle1_pos, paddle2_pos, ball_pos, ball_vel, pad_vel,pad2_vel,pt1,pt2

    #controls ball reflection
    #left side controls
    if ball_pos[0] <= (BALL_RADIUS + 8):
        if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[0] :
            ball_vel[0] = - ball_vel[0]
        elif  ball_pos[1] <= paddle2_pos[1] or ball_pos[1] >= paddle2_pos[0] :
            p2score()
            ball_initl()
    #right side controls
    elif ball_pos[0] >= 572:
        if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[0] :
            ball_vel[0] = - ball_vel[0]
        elif ball_pos[1] <= paddle2_pos[1] or ball_pos[1] >= paddle2_pos[0] :
            p1score()
            ball_initr()
        
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= 380:
        ball_vel[1] = - ball_vel[1]
        
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # update paddle's vertical position, keep paddle on the screen 
    #paddle 1
    paddle1_pos[0] += pad_vel
    paddle1_pos[1] += pad_vel
    if paddle1_pos[0] > 400:
        paddle1_pos[0] = 400
        paddle1_pos[1] = 320
        pad_vel = 0 
    elif paddle1_pos[1] < 0:
        paddle1_pos[0] = 80
        paddle1_pos[1] = 0
        pad_vel = 0
    
    #paddle 2    
    paddle2_pos[0] += pad2_vel
    paddle2_pos[1] += pad2_vel
    if paddle2_pos[0] > 400:
        paddle2_pos[0] = 400
        paddle2_pos[1] = 320
        pad2_vel = 0 
    elif paddle2_pos[1] < 0:
        paddle2_pos[0] = 80
        paddle2_pos[1] = 0
        pad2_vel = 0
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
# draw paddles
    # player 1
    canvas.draw_line((5, paddle1_pos[0]) , (5, paddle1_pos[1]) , PAD_WIDTH, "Red")
    
    # player 2
    canvas.draw_line((595, paddle2_pos[0]), (595,paddle2_pos[1]), PAD_WIDTH, "Red")
           
    # draw ball and scores
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_text(score, (265, 40), 50, "Red")
    
def keydown(key):
    global pad_vel, pad2_vel
    acc = 1
    add = 1
    #right side
    if key==simplegui.KEY_MAP["down"]:
        pad2_vel += acc
    if key==simplegui.KEY_MAP["up"]:
        pad2_vel -= acc
     #left side 
    if key==simplegui.KEY_MAP["s"]:
        pad_vel += add
    if key==simplegui.KEY_MAP["w"]:
        pad_vel -= add
   
def keyup(key):
    global pad_vel, pad2_vel
    abb=1
    
    if key==simplegui.KEY_MAP["up"]:
       pass
    if key==simplegui.KEY_MAP["down"]:
        pass
    if key==simplegui.KEY_MAP["w"]:
       pass
    if key==simplegui.KEY_MAP["s"]:
        pass

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart)


# start frame
frame.start()
