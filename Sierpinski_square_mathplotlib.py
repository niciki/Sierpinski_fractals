import matplotlib.pyplot as plt
import random as R

n  = 1000000

vertex_coordinates = [[-200,-100], [-200, 300], [200,-100], [200, 300], [-200, 100], [0, -100], [0, 300], [200, 100]]
x_coordinates = [vertex_coordinates[0][0]]
y_coordinates = [vertex_coordinates[0][1]]
for i in range(n):
    r = R.randrange(8)
    x_coordinates.append((x_coordinates[-1] + 2 * vertex_coordinates[r][0]) / 3)
    y_coordinates.append((y_coordinates[-1] + 2 * vertex_coordinates[r][1]) / 3)
fig, ax = plt.subplots()
ax.scatter(x_coordinates, y_coordinates, s = 0.1)
ax.set(title=f'Sierpinski square for {n} points')
plt.show()
