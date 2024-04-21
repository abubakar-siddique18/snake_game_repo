import turtle
import time
import random

DELAY = 0.1  # to control the speed of the game


win = turtle.Screen()  # sets up the game window
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=700, height=700)
win.tracer(0)  # Turns off the screen updates

# Score display
score_display = turtle.Turtle()       # to display the score at the top of the window
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

# Initializing score to zero
score = 0

# Functions
def display_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def game_over():
    global score
    win.onkeypress(None, "Up")
    win.onkeypress(None, "Down")
    win.onkeypress(None, "Left")
    win.onkeypress(None, "Right")
    win.update()
    score_display.clear()
    score_display.write(f"Game Over! Your Final Score: {score}", align="center", font=("Courier", 24, "normal"))
    time.sleep(1)
    
# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

all_new_tails = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def check_collision():
    global score
    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a segment to the snake
        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("square")
        new_tail.color("blue")
        new_tail.penup()
        all_new_tails.append(new_tail)

        # Increase the score
        score += 10
        display_score()

    # Check for collision with walls
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        game_over()

    # Check for collision with the snake's own body
    for tail in all_new_tails:
        if tail.distance(head) < 20:
            game_over()

# Keyboard onpress keys
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Main game loop
while True:
    win.update()

    # Move the snake
    move()

    # Check for collisions
    check_collision()

    # Move the end segments first in reverse order
    for index in range(len(all_new_tails) - 1, 0, -1):
        x = all_new_tails[index - 1].xcor()
        y = all_new_tails[index - 1].ycor()
        all_new_tails[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(all_new_tails) > 0:
        x = head.xcor()
        y = head.ycor()
        all_new_tails[0].goto(x, y)

    time.sleep(DELAY)