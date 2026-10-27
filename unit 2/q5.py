import numpy as np

arr = np.array([25, 40, 55, 60, 75, 80, 90, 100,
                110, 120, 135, 140, 150, 160, 175, 180,
                190, 200, 220, 240, 250, 275, 300, 350])

print(arr)
re_shape = arr.reshape(6,4)
print(arr.shape)
print(re_shape.shape)