
import numpy as np

purchases = np.array([250, 500, 1200, 800, 1500, 300, 450, 2000])

# Display purchases greater than ₹1000
print("Purchases greater than 1000:")
print(purchases[purchases > 1000])

# Find mean purchase amount
print("Mean Purchase Amount:", np.mean(purchases))

# Add cashback of ₹100 using broadcasting
cashback = purchases + 100
print("Purchases after Cashback:")
print(cashback)
