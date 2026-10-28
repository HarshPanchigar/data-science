import numpy as np

# Heights of 15 people in cm
heights = np.array([150, 162, 175, 168, 155, 180, 172, 160,
                    185, 158, 170, 177, 165, 190, 152])

maximum = np.max(heights)
minimum = np.min(heights)

Scaling = (heights - minimum) / (maximum - minimum)
print(Scaling)