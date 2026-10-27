import numpy as np

prices = np.array([
    150, 250, 350, 450, 500,
    600, 750, 800, 900, 1000,
    1200, 1350, 1500, 1750, 2000,
    2200, 2500, 2800, 3000, 3500
])

print(prices)
print(prices[prices > 2000])
print(prices[(prices > 1000) & (prices < 2000)])