import turtle
from myFunctionfile import*
turtle.colormode(255)
bob = turtle.Turtle()
turtle.bgcolor("black")
bob.width(10)
bob.color("red")
bob.speed(11)

for times in range(10):
     
     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(-100,-100)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(100,100)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(-400,-400)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(400,400)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(500,-400)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(-500,-200)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(550,550)
     bob.forward(50)
     bob.pendown()
     
     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(500,100)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(-500,300)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(-300,100)
     bob.forward(50)
     bob.pendown()

     star(bob,times*10+8,"red")
     bob.penup()
     bob.right(30)
     bob.goto(300,-400)
     bob.forward(50)
     bob.pendown()

     
     
     

    

     
     
     
     
