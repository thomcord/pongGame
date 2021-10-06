
import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#Bar A
bar_a = turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
bar_a.color("white")
bar_a.shapesize(stretch_wid=5, stretch_len=1)
bar_a.penup()
bar_a.goto(-350, 0)


#Bar B
bar_b = turtle.Turtle()
bar_b.speed(0)
bar_b.shape("square")
bar_b.color("white")
bar_b.shapesize(stretch_wid=5, stretch_len=1)
bar_b.penup()
bar_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

#



#Functions
def bar_a_up():
    y = bar_a.ycor()
    y += 20
    bar_a.sety(y)

def bar_a_down():
    y = bar_a.ycor()
    y -= 20
    bar_a.sety(y)

def bar_b_up():
    y = bar_b.ycor()
    y += 20
    bar_b.sety(y)

   
def bar_b_down(): 
    y = bar_b.ycor()
    y -= 20
    bar_b.sety(y)

#Keyboard
wn.listen()
wn.onkeypress(bar_a_up, "w")
wn.onkeypress(bar_a_down, "s")
wn.onkeypress(bar_b_up, "Up")
wn.onkeypress(bar_b_down, "Down")


#Game Loop
while True:
    wn.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1


    #bar/ball colision

    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < bar_b.ycor() + 40 and ball.ycor() > bar_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < bar_a.ycor() + 40 and ball.ycor() > bar_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1