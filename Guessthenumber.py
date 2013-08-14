import random
import math
import simplegui

#global variables
secretnumber = random.randrange(0, 100)
guess = -1
guesses = 7

#Processes input / guess
def inputt(text):
    global guess
    guess = int(text)
    print 'You guessed', guess
    range100()
    

    
#initialize 0-99 game    
def init():
    global guesses
    global guess
    global secretnumber
    guess = -1
    guesses = 7
    secretnumber = random.randrange(0, 100)
    range100()

#initialize 0-999 game    
def init2():
    global guesses
    global guess
    global secretnumber
    guess = -1
    guesses = 10
    secretnumber = random.randrange(0, 100)
    range1000()
    
def range100():
    # declare globals
    global guesses
    global guess
    
    #the guess system
    if guess == -1 :
        print ''
        print 'New Game'
        print 'Please enter a number between 0 and 99.'
        print 'You have 7 guesses.' 
        print ''
    elif guess == secretnumber :
        print 'You Win!'
        init()
    elif guesses == 1 :
        print 'You have no more guesses left. You lose.'
        init()
    elif guess < secretnumber :
        guesses -=1
        print 'Higher'
        print 'You have', guesses , 'guesses remaining.'
        print ''
    elif guess > secretnumber :
        guesses -=1
        print 'Lower!'
        print 'You have', guesses , 'guesses remaining.'
        print ''
        
def range1000():
    #declare globals
    global guesses
    global guess
    global secretnumber
    
    secretnumber = random.randrange(0,1000)
    
    #the guess system
    if guess == -1 :
        print ''
        print 'New Game'
        print 'Please enter a number between 0 and 999.'
        print 'You have 10 guesses.'
    elif guess == secretnumber2 :
        print 'You Win!'
        init2()
    elif guesses == 1 :
        print 'You have no more guesses left. You lose.'
        init2()
    elif guess < secretnumber2 :
        guesses -=1
        print 'Higher'
        print 'You have', guesses , 'guesses remaining.'
        print ''
    elif guess > secretnumber2 :
        guesses -=1
        print 'Lower!'
        print 'You have', guesses , 'guesses remaining.'
        print ''

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Range is [0,100)", init, 200)
frame.add_button("Range is [0,1000)", init2, 200)
frame.add_input("Enter a Guess:", inputt, 200)

#initialize game for first run
init()
# Start the frame animation
frame.start()
