# print(2+2)
# print("\n") :: for newline character

# Rules of the game:
# -- Any live cell with fewer than two live neighbours dies, as if casued by underpopulation.
# -- Any live cell with two or three live neighbours lives on to the next generation.
# --Any live cell with more than three neighbours dies, as if by overpopulation.
# --Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import numpy as np
import matplotlib.pyplot as plt
# Declare a 2D matrix of an arbitrary size, say 10 x 10
l = np.zeros(shape = (50,50), dtype = np.int)

# Initialize the 2D matrix with an initial condition
# ----- The following is the initial condition for a Glider -----
l[4,4] = 1
l[5,5] = 1
l[6,3] = 1
l[6,4] = 1
l[6,5] = 1

# Start the loop: FOR or WHILE: Justify which is better of the two and why?
for i in range(0,50):
for j in range(0,50):

# Update the 2D matrix according to the rules specified by the Game of Life.

# Plot the current state of the 2D matrix using MATPLOTLIB
plt.matshow(l)
#plt.grid()
plt.show()
# Press 'key' to continue until FOR or WHILE loop allows

# Close All windows

# Print Game Over!



