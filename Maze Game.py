import turtle
import time
import sys

# Screen
wn = turtle.Screen()
wn.title("I have no clue what this is going to be")
wn.bgcolor("Light Blue")
wn.setup(width=1920, height=1080)
wn.tracer(0)

# Start
start_one = turtle.Turtle()
start_one.shape("square")
start_one.color("lime")
start_one.shapesize(stretch_wid=4, stretch_len=4)
start_one.penup()
start_one.goto(-850, -450)

# End
end_one = turtle.Turtle()
end_one.shape("square")
end_one.color("lime")
end_one.shapesize(stretch_wid=4, stretch_len=4)
end_one.penup()
end_one.goto(850, -450)

# Player
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(-850, -450)

# Text

# Function
def player_up():
    y = player.ycor()
    y += 20
    player.sety(y)


def player_down():
    y = player.ycor()
    y -= 20
    player.sety(y)


def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def player_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# MAZE BOARDER
# 1
one = turtle.Turtle()
one.hideturtle()
one.penup()
one.goto(-900, -500)
one.width(20)
one.color("black")
one.pendown()
one.forward(1800)

# 2
two = turtle.Turtle()
two.hideturtle()
two.penup()
two.goto(900, -500)
two.width(20)
two.color("black")
two.left(90)
two.pendown()
two.forward(1000)

# 3
three = turtle.Turtle()
three.hideturtle()
three.penup()
three.goto(900, 500)
three.width(20)
three.color("black")
three.left(180)
three.pendown()
three.forward(1800)

# 4
four = turtle.Turtle()
four.hideturtle()
four.penup()
four.goto(-900, 500)
four.width(20)
four.color("black")
four.right(90)
four.pendown()
four.forward(1000)

# The Maze
# wall 1
wall_one = turtle.Turtle()
wall_one.hideturtle()
wall_one.penup()
wall_one.goto(-800, -500)
wall_one.width(20)
wall_one.color("black")
wall_one.left(90)
wall_one.pendown()
wall_one.forward(900)

# wall 2
wall_two = turtle.Turtle()
wall_two.hideturtle()
wall_two.penup()
wall_two.goto(-700, 500)
wall_two.width(20)
wall_two.color("black")
wall_two.right(90)
wall_two.pendown()
wall_two.forward(900)

# wall 3
wall_three = turtle.Turtle()
wall_three.hideturtle()
wall_three.penup()
wall_three.goto(-600, -500)
wall_three.width(20)
wall_three.color("black")
wall_three.left(90)
wall_three.pendown()
wall_three.forward(900)

# wall 4
wall_four = turtle.Turtle()
wall_four.hideturtle()
wall_four.penup()
wall_four.goto(-500, 500)
wall_four.width(20)
wall_four.color("black")
wall_four.right(90)
wall_four.pendown()
wall_four.forward(900)

# wall 5
wall_five = turtle.Turtle()
wall_five.hideturtle()
wall_five.penup()
wall_five.goto(-400, -500)
wall_five.width(20)
wall_five.color("black")
wall_five.left(90)
wall_five.pendown()
wall_five.forward(900)

# wall 6
wall_six = turtle.Turtle()
wall_six.hideturtle()
wall_six.penup()
wall_six.goto(-300, 500)
wall_six.width(20)
wall_six.color("black")
wall_six.right(90)
wall_six.pendown()
wall_six.forward(900)

# wall 7
wall_seven = turtle.Turtle()
wall_seven.hideturtle()
wall_seven.penup()
wall_seven.goto(-200, -500)
wall_seven.width(20)
wall_seven.color("black")
wall_seven.left(90)
wall_seven.pendown()
wall_seven.forward(900)

# wall 8
wall_eight = turtle.Turtle()
wall_eight.hideturtle()
wall_eight.penup()
wall_eight.goto(-100, 500)
wall_eight.width(20)
wall_eight.color("black")
wall_eight.right(90)
wall_eight.pendown()
wall_eight.forward(900)

# wall 9
wall_nine = turtle.Turtle()
wall_nine.hideturtle()
wall_nine.penup()
wall_nine.goto(0, -500)
wall_nine.width(20)
wall_nine.color("black")
wall_nine.left(90)
wall_nine.pendown()
wall_nine.forward(900)

# wall 10
wall_ten = turtle.Turtle()
wall_ten.hideturtle()
wall_ten.penup()
wall_ten.goto(0, -500)
wall_ten.width(20)
wall_ten.color("black")
wall_ten.left(90)
wall_ten.pendown()
wall_ten.forward(900)

# wall 11
wall_eleven = turtle.Turtle()
wall_eleven.hideturtle()
wall_eleven.penup()
wall_eleven.goto(100, 500)
wall_eleven.width(20)
wall_eleven.color("black")
wall_eleven.right(90)
wall_eleven.pendown()
wall_eleven.forward(900)

# wall twelve
wall_twelve = turtle.Turtle()
wall_twelve.hideturtle()
wall_twelve.penup()
wall_twelve.goto(200, -500)
wall_twelve.width(20)
wall_twelve.color("black")
wall_twelve.left(90)
wall_twelve.pendown()
wall_twelve.forward(900)

# wall thirteen
wall_thirteen = turtle.Turtle()
wall_thirteen.hideturtle()
wall_thirteen.penup()
wall_thirteen.goto(300, 500)
wall_thirteen.width(20)
wall_thirteen.color("black")
wall_thirteen.right(90)
wall_thirteen.pendown()
wall_thirteen.forward(900)

# wall fourteen
wall_fourteen = turtle.Turtle()
wall_fourteen.hideturtle()
wall_fourteen.penup()
wall_fourteen.goto(300, 500)
wall_fourteen.width(20)
wall_fourteen.color("black")
wall_fourteen.right(90)
wall_fourteen.pendown()
wall_fourteen.forward(900)

# wall fifteen
wall_fifteen = turtle.Turtle()
wall_fifteen.hideturtle()
wall_fifteen.penup()
wall_fifteen.goto(400, -500)
wall_fifteen.width(20)
wall_fifteen.color("black")
wall_fifteen.left(90)
wall_fifteen.pendown()
wall_fifteen.forward(900)

# wall sixteen
wall_sixteen = turtle.Turtle()
wall_sixteen.hideturtle()
wall_sixteen.penup()
wall_sixteen.goto(500, 500)
wall_sixteen.width(20)
wall_sixteen.color("black")
wall_sixteen.right(90)
wall_sixteen.pendown()
wall_sixteen.forward(900)

# wall seventeen
wall_seventeen = turtle.Turtle()
wall_seventeen.hideturtle()
wall_seventeen.penup()
wall_seventeen.goto(600, -500)
wall_seventeen.width(20)
wall_seventeen.color("black")
wall_seventeen.left(90)
wall_seventeen.pendown()
wall_seventeen.forward(900)

# wall eighteen
wall_eighteen = turtle.Turtle()
wall_eighteen.hideturtle()
wall_eighteen.penup()
wall_eighteen.goto(700, 500)
wall_eighteen.width(20)
wall_eighteen.color("black")
wall_eighteen.right(90)
wall_eighteen.pendown()
wall_eighteen.forward(900)

# wall nineteen
wall_nineteen = turtle.Turtle()
wall_nineteen.hideturtle()
wall_nineteen.penup()
wall_nineteen.goto(800, -500)
wall_nineteen.width(20)
wall_nineteen.color("black")
wall_nineteen.left(90)
wall_nineteen.pendown()
wall_nineteen.forward(900)

# wall twenty
wall_twenty = turtle.Turtle()
wall_twenty.hideturtle()
wall_twenty.penup()
wall_twenty.goto(900, 500)
wall_twenty.width(20)
wall_twenty.color("black")
wall_twenty.right(90)
wall_twenty.pendown()
wall_twenty.forward(900)

# Keybindings aka controls
wn.listen()
wn.onkeypress(player_up, "w")
wn.onkeypress(player_down, "s")
wn.onkeypress(player_left, "a")
wn.onkeypress(player_right, "d")


# Main game loop
while True:
    wn.update()

# Boarder Detection (Outer walls)

    if player.xcor() > 880:
        player.setx(880)

    if player.xcor() < -880:
        player.setx(-880)
#                                   v
    if player.ycor() < -480 and player.xcor() < -880:
        player.sety(-480)

    if player.ycor() > 480:
        player.sety(480)
#            v
    if player.ycor() < -500:
        player.setx(880)

    # wall 1 collision
    if player.ycor() < 400 and player.xcor() < -795 and player.xcor() > -820:
        player.setx(-820)

    if player.ycor() < 400 and player.xcor() < -775 and player.xcor() > -800:
        player.setx(-775)

    # wall 2 collision
    if player.ycor() > -400 and player.xcor() < -695 and player.xcor() > -720:
        player.setx(-720)

    if player.ycor() > -400 and player.xcor() < -675 and player.xcor() > -700:
        player.setx(-675)

    # wall 3 collision
    if player.ycor() < 400 and player.xcor() < -595 and player.xcor() > -620:
        player.setx(-620)

    if player.ycor() < 400 and player.xcor() < -575 and player.xcor() > -600:
        player.setx(-575)

    # wall 4 collision
    if player.ycor() > -400 and player.xcor() < -495 and player.xcor() > -520:
        player.setx(-520)

    if player.ycor() > -400 and player.xcor() < -475 and player.xcor() > -500:
        player.setx(-475)

    # wall 5 collision
    if player.ycor() < 400 and player.xcor() < -395 and player.xcor() > -420:
        player.setx(-420)

    if player.ycor() < 400 and player.xcor() < -375 and player.xcor() > -400:
        player.setx(-375)

    # wall 6 collision
    if player.ycor() > -400 and player.xcor() < -295 and player.xcor() > -320:
        player.setx(-320)

    if player.ycor() > -400 and player.xcor() < -275 and player.xcor() > -300:
        player.setx(-275)

    # wall 7 collision
    if player.ycor() < 400 and player.xcor() < -195 and player.xcor() > -220:
        player.setx(-220)

    if player.ycor() < 400 and player.xcor() < -175 and player.xcor() > -200:
        player.setx(-175)

    # wall 8 collision
    if player.ycor() > -400 and player.xcor() < -95 and player.xcor() > -120:
        player.setx(-120)

    if player.ycor() > -400 and player.xcor() < -75 and player.xcor() > -100:
        player.setx(-75)

    # wall 9 collision
    if player.ycor() < 400 and player.xcor() < 5 and player.xcor() > -20:
        player.setx(-20)

    if player.ycor() < 400 and player.xcor() < 25 and player.xcor() > -0:
        player.setx(25)

    # wall 10 collision
    if player.ycor() > -400 and player.xcor() < 105 and player.xcor() > 80:
        player.setx(80)

    if player.ycor() > -400 and player.xcor() < 125 and player.xcor() > 100:
        player.setx(125)

    # wall 11 collision
    if player.ycor() < 400 and player.xcor() < 205 and player.xcor() > 180:
        player.setx(180)

    if player.ycor() < 400 and player.xcor() < 225 and player.xcor() > 200:
        player.setx(225)

    # wall 12 collision
    if player.ycor() > -400 and player.xcor() < 305 and player.xcor() > 280:
        player.setx(280)

    if player.ycor() > -400 and player.xcor() < 325 and player.xcor() > 300:
        player.setx(325)

    # wall 13 collision
    if player.ycor() < 400 and player.xcor() < 405 and player.xcor() > 380:
        player.setx(380)

    if player.ycor() < 400 and player.xcor() < 425 and player.xcor() > 400:
        player.setx(425)

    # wall 14 collision
    if player.ycor() > -400 and player.xcor() < 505 and player.xcor() > 480:
        player.setx(480)

    if player.ycor() > -400 and player.xcor() < 525 and player.xcor() > 500:
        player.setx(525)

    # wall 15 collision
    if player.ycor() < 400 and player.xcor() < 605 and player.xcor() > 580:
        player.setx(580)

    if player.ycor() < 400 and player.xcor() < 625 and player.xcor() > 600:
        player.setx(625)

    # wall 16 collision
    if player.ycor() > -400 and player.xcor() < 705 and player.xcor() > 680:
        player.setx(680)

    if player.ycor() > -400 and player.xcor() < 725 and player.xcor() > 700:
        player.setx(725)

    # wall 17 collision
    if player.ycor() < 400 and player.xcor() < 805 and player.xcor() > 780:
        player.setx(780)

    if player.ycor() < 400 and player.xcor() < 825 and player.xcor() > 800:
        player.setx(825)

    # wall 18 collision
    if player.ycor() > -400 and player.xcor() < 905 and player.xcor() > 880:
        player.setx(880)

    if player.ycor() > -400 and player.xcor() < 925 and player.xcor() > 900:
        player.setx(925)

    # wall 19 collision
    if player.ycor() < 400 and player.xcor() < 1005 and player.xcor() > 980:
        player.setx(980)

    if player.ycor() < 400 and player.xcor() < 1025 and player.xcor() > 1000:
        player.setx(1025)

    # wall 20 collision
    if player.ycor() < 400 and player.xcor() < 1105 and player.xcor() > 1080:
        player.setx(1080)

    if player.ycor() < 400 and player.xcor() < 1125 and player.xcor() > 1100:
        player.setx(1125)

    # end of the level (Just a test and doesn't work yet)
    if 850 < player.xcor() < 854 and -450 < player.ycor() < -454:
        player.setx(1125)






