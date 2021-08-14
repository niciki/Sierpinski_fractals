import matplotlib.pyplot as plt
import random as R

n = 10000

vertex_coordinates = [[-200.0, -100.0], [0.0, 200.0], [200.0, -100.0]]
x_coordinates = [vertex_coordinates[0][0]]
y_coordinates = [vertex_coordinates[0][1]]
for i in range(n):
    r = R.randrange(3)
    x_coordinates.append((x_coordinates[-1] + vertex_coordinates[r][0]) / 2)
    y_coordinates.append((y_coordinates[-1] + vertex_coordinates[r][1]) / 2)
fig, ax = plt.subplots()
ax.scatter(x_coordinates, y_coordinates, s = 0.1)
ax.set(title=f'Sierpinski triangle for {n} points')
plt.show()
