import numpy as np

production = np.array([
    120, 135, 140, 125, 150,
    160, 145, 130, 155, 170,
    165, 180, 175, 150, 140,
    190, 185, 160, 155, 200
])

print(production)
print(np.mean(production))
print(np.median(production))
print(np.std(production))
print(np.min(production))
print(np.max(production))