import numpy as np

ages = np.array([
    18, 22, 25, 30, 35, 28,
    40, 45, 32, 27, 50, 38,
    42, 24, 33, 29, 55, 36
])

print(ages)
print(ages[ages > 40])
print(ages[ages < 25])