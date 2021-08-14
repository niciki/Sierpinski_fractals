import random as R
import turtle as T

n = 10000

T.hideturtle()
T.speed(0)
vertex_coordinates = [[-200,-100], [-200, 300], [200,-100], [200, 300], [-200, 100], [0, -100], [0, 300], [200, 100]]
x, y = vertex_coordinates[0]
for i in range(n):
    r = R.randrange(8)
    x_ = (x + 2 * vertex_coordinates[r][0]) / 3
    y_ = (y + 2 * vertex_coordinates[r][1]) / 3
    T.penup()
    T.goto(x_, y_)
    T.pendown()
    x, y = x_, y_
    T.dot(2)
T.done()
