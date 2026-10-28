import numpy as np

scores = np.array([
    78, 85, 92, 67, 88,
    74, 95, 81, 69, 90,
    76, 84, 72, 96, 87,
    65, 79, 91, 83, 77,
    89, 70, 94, 82, 86
])

print(scores)
print(np.sort(scores[scores >= 80]))
print(np.average(scores))
print(scores+5)