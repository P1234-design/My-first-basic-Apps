import numpy as np

#A => 3x+y = 9
#B => x+2Y = 8

A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])

print("Matrix A:")
print(A)

print("\nVector B:")
print(B)

solution = np.linalg.solve(A, B)

print("\nSolution [x, y]:",solution)
