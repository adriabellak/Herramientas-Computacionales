"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

import random
from random import randrange
from turtle import *
from freegames import vector

state = {'score': 0, 'lives': 3}
liveswriter1 = Turtle(visible=False)
scorewriter = Turtle(visible=False)
path = Turtle(visible=False)
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
colors = ['blue','pink','black','purple','green']
ballcolor = random.choice(colors)
colors.remove(ballcolor)
targetcolor = random.choice(colors)

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199

        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, targetcolor)

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, ballcolor)

    update()

def move():
    "Move ball and targets."
    # Generate a new target at random times
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move the existing targets
    for target in targets:
        target.x -= 2

    # Move the cannon shot
    if inside(ball):
        speed.y -= 1
        ball.move(speed)

    # Make a copy of the existing target list before redrawing
    dupe = targets.copy()
    targets.clear()

    # Detect if the bullet hits a target
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else: 
            state['score'] += 1
    scorewriter.undo()
    scorewriter.write(f"Score: {state['score']}")
    draw()

    # Indicate number of lives
    lives = 3

    # Detect when a target reaches the left side
    for target in targets:
        if not inside(target):
            #targets.remove(target)
            lives = lives - 1
            state['lives'] = lives
            liveswriter1.undo()
            liveswriter1.write(f"Lives: {state['lives']}")
            if lives == 0:
                return
    
    liveswriter1.undo()
    liveswriter1.write(f"Lives: {state['lives']}")
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
scorewriter.up()
scorewriter.goto(150,150)
scorewriter.down()
scorewriter.write(f"Score: {state['score']}")
liveswriter1.up()
liveswriter1.goto(-150,150)
liveswriter1.down()
liveswriter1.write(f"Lives: {state['lives']}")
tracer(False)
onscreenclick(tap)
move()
done()
