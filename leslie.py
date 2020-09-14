''' Homework 2 for Math/EEB 681

Instructions: fill in the code below following the instructions in the comments.
'''

import numpy as np
from numpy.linalg import matrix_power, eig

# There are 6 age classes: newborns, young juveniles, juveniles, early adults, 
#   middle-age adults, older adults
# Fecundity rates (in that order) are:
F = np.array([0, 0, 0, 5, 2, 0])
# Survival probabilities for each class are:
P = np.array([0.4, 0.6, 0.7, 0.9, 0.8, 0])
# Starting population numbers (time t=0) are:
N0 = np.array([100, 60, 60, 40, 30, 10])

# Create a 6x6 Leslie matrix below. Use np.zeros to create a starting matrix,
#   and then fill in the non-zero entries either with a for-loop or by making
#   use of the matrix structure. DO NOT hardcode an element-by-element assignment
#   of matrix entries!



# Run your model for 100 time steps (time t=100) using matrix-vector multiplication.
#   (Note: you can use matrix_power to do this faster than a for-loop)



# Sum the number of adults, rounding to the nearest integer. Print this number
#   to the terminal.


# Using eig, print the eigenvalues (but leave out the eigenvectors) of the leslie matrix


