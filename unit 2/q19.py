
import numpy as np

# Create first 4 x 4 matrix
A = []
print("Enter values for Matrix A:")
for i in range(4):
    row = list(map(int, input("Enter 4 numbers: ").split()))
    A.append(row)

# Create second 4 x 4 matrix
B = []
print("Enter values for Matrix B:")
for i in range(4):
    row = list(map(int, input("Enter 4 numbers: ").split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

# Element-wise addition
print("\nAddition:")
print(A + B)

# Element-wise subtraction
print("\nSubtraction:")
print(A - B)

# Element-wise multiplication
print("\nMultiplication:")
print(A * B)
