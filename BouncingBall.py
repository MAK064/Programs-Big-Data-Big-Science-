from JMSSGraphics import *
import random

# Dimentions
width = 1200
height = 800
fps = 30

jmss = Graphics(width = width, height = height, title = "Bouncing Ball", fps = fps)

#Setting Initail Variables (Randomly)
BallX = random.randint(1, (height - 65))
BallY = random.randint(1, (height - 65))

momentum = random.uniform(0, 10)
G = random.uniform(1, -1)
TFall = random.uniform(-50, 50)

if (random.randint(0, 1) == 1):
    direction = 1
else:
    direction = -1

#Debug Tools
print (direction)
print (momentum)
print (G)
print (TFall)
print ("(" + str(BallX) + ", " + str(BallY) + ")")

#Loads ball into memory
ball = jmss.loadImage("ball.png")

#The main loop that is executed every frame
@jmss.mainloop
def simulation():
    global BallX, BallY, TFall, G, width, direction, momentum

    if jmss.isKeyDown(KEY_UP):
        G += 1/60
    if jmss.isKeyDown(KEY_DOWN):
        G -= 1/60
    if jmss.isKeyDown(KEY_LEFT):
        momentum -= 0.1
    if jmss.isKeyDown(KEY_RIGHT):
        momentum += 0.1

    #Does logic for the ball when inbetween top and bottom of screen
    if 0 < BallY < (height - 64):
        BallX += direction*momentum
        BallY += G*TFall

    #Does logic for the ball when above top of screen
    if BallY > (height - 64):
        TFall = TFall*(-0.98)
        BallX += direction * momentum
        BallY = height - 65

    #Does logic for the ball when below screen
    if BallY < 0:
        TFall = TFall*(-0.98)
        BallX += direction * momentum
        BallY = 1

    #Logic for x direcion reversal
    if (0 > BallX or BallX > (width - 64)):
        direction = direction*(-1)

    #Clears screen to be drawn
    jmss.clear(0,0,0,1)

    #Draws the ball from memor
    jmss.drawImage( ball , x = BallX, y = BallY)

    #Draws text onscreen displaying info
    jmss.drawText("Ball's Position is: (" + str(int(BallX)) + ", " + str(int(BallY)) + ")" , x = 0, y = 0)
    jmss.drawText("G = " + str(G/(2/6)*-1)  , x = width - 68, y = 0)
    jmss.drawText("Ball's sideways momentum is ~ " + str(int(momentum)) , x = width - 205, y = 12)


    #Increment timefalling
    TFall += 1

jmss.run()
