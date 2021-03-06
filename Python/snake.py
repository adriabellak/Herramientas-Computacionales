"""
Team members
Alejandro Pascal Garza, A01023621
Santiago Villalobos, A01028142
Adriana Abella Kuri, A01329591

Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
import random
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['blue','pink','black','purple','green']
snakecolor = random.choice(colors)
colors.remove(snakecolor)
foodcolor = random.choice(colors)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():

    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakecolor)

    square(food.x, food.y, 9, foodcolor)
    update()
    ontimer(move, 100)

def movefood():
    "Move food one place in random direction"
    if food.x == -200:
        xdirections = [0, 10]
    elif food.x == 190:
        xdirections = [-10, 0]
    else:
        xdirections = [-10, 0, 10]

    if food.y == -200:
        ydirections = [0, 10]
    elif food.y == 190:
        ydirections = [-10, 0]
    else:
        ydirections = [-10, 0, 10]

    food.x = food.x + random.choice(xdirections)
    food.y = food.y + random.choice(ydirections)
    ontimer(movefood, 500)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movefood()
done()
