import random as R
import turtle as T

T.hideturtle()
T.speed(0)
vertex_coordinates = [[-200,-100], [0,200], [200,-100]]
x, y = vertex_coordinates[0]
for i in range(100000):
    r = R.randrange(3)
    x_ = (x + vertex_coordinates[i][0]) / 2
    y_ = (y + vertex_coordinates[i][1]) / 2
    T.penup()
    T.goto(x_, y_)
    T.pendown()
    x, y = x_, y_
    T.dot(2)
T.done()
