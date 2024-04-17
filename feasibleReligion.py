"""
12. Consider the following small instance of the linear programming problem:
maximize   3x + 5y
subject to


x+ y≤4
x + 3y ≤ 6
x ≥ 0, y ≥ 0.

a. Sketch, in the Cartesian plane, the problem’s feasible region, deﬁned as
the set of points satisfying all the problem’s constraints.

b. Identify the region’s extreme points.

c. Solve this optimization problem by using the following theorem: A linear
programming problem with a nonempty bounded feasible region always
has a solution, which can be found at one of the extreme points of its
feasible region    
    """
import numpy as np
import matplotlib.pyplot as plt

# Define the constraints
x = np.linspace(0, 10, 400)
y1 = 4 - x
y2 = (6 - x) / 3

# Plot the constraints
plt.plot(x, y1, label=r'$x + y \leq 4$')
plt.fill_between(x, 0, y1, alpha=0.1)

plt.plot(x, y2, label=r'$x + 3y \leq 6$')
plt.fill_between(x, 0, y2, alpha=0.1)

# Plot the axes
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.xlim(0, 5)
plt.ylim(0, 2)

plt.xlabel('x')
plt.ylabel('y')

plt.title('Feasible Region')

# Identify the extreme points
extreme_points = [(0, 0), (0, 2), (3, 1), (4, 0)]
for point in extreme_points:
    plt.plot(point[0], point[1], 'ro')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})')

plt.legend()
plt.grid()
plt.show()
