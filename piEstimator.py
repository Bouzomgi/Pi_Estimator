

from matplotlib.pyplot import *
from numpy import *
from random import *
from matplotlib.animation import *

total, inside = 0, 0

fig = figure()
ax = axes(xlim=(0, 1), ylim=(0, 1))
x = linspace(0, 1, 100)

plot(x, (1 - (x**2))**0.5, color = 'black')

#OR make a list like x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#h = [(1 - (i**2)))**0.5 for i in x]
#plot(x, h, color = 'black')

title("Monte Carlo Pi Estimator")

def createPoint():
	return(random(), random())

def isInsideCircle(point):
	return (point[0] ** 2) + (point[1] ** 2) <= 1

def animate(i):
	global inside
	global total

	point = createPoint()
	color = "blue" if isInsideCircle(point) else "red"
	inside += 1 if isInsideCircle(point) else 0
	total += 1
	scatter(point[0], point[1], c = color)
	piApprox = format(4 * (inside / total), '.4f')

	ax.set_xlabel(f'Pi approximation: {piApprox}')


ani = FuncAnimation(fig, animate, interval=10)

show()


