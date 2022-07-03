from turtle import *
speed(0)
setup(700, 650)
bgcolor('black')
pencolor('violet')
pensize(3)

for item in range(10):
    rad=150
    for i in range(36):
        circle(rad)
        rad-=4
    right(36)
hideturtle()
done()