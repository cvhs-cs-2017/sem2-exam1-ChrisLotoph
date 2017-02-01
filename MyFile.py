n = int(input('Enter a number '))
def addten(n):
    n = n + 10
    return (n)
print (addten(n))


x = int(input('Enter a new number '))
import turtle
bob=turtle.Turtle()

for i in range(100):
    bob.forward(x)
    bob.left(3.6)



import turtle
turtle = turtle.Turtle()
Anyturtle = 100
l = 90
w = 80
def DrawRectangle(Anyturtle,l,w):
    turtle.forward(Anyturtle)
    turtle.left(l)
    turtle.forward(w)
    turtle.left(l)
    turtle.forward(Anyturtle)
    turtle.left(l)
    turtle.forward(w)
DrawRectangle(Anyturtle,l,w)
