import numpy as np

# Quarterly sales of 24 branches
sales = np.array([
    55000, 72000, 85000, 91000,
    68000, 78000, 82000, 95000,
    60000, 88000, 105000, 76000,
    99000, 84000, 73000, 110000,
    67000, 92000, 80000, 87000,
    115000, 79000, 96000, 70000
])

print(sales)
matrix = sales.reshape(6, 4)

print("Sales Matrix:")
print(matrix)
print(sales[sales > 80000])

print(np.mean(sales))
print(np.max(sales))
print(np.min(sales))

flat = matrix.ravel()

print("\nFlattened Array:")
print(flat)