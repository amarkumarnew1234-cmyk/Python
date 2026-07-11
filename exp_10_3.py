#3. Perform Matrix multiplication of any 2 n*n matrices.
import numpy as np
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
result = np.dot(matrix_a, matrix_b)
print("Result of Matrix Multiplication:\n", result)
