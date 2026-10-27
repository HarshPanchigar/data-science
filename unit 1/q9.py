# Customer IDs of two e-commerce websites
store1 = {101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115}

store2 = {108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122}

# 1. Union
print("Union:", store1.union(store2))

# 2. Intersection
print("Intersection:", store1.intersection(store2))

# 3. Customers unique to each store
print("Unique to Store 1:", store1 - store2)
print("Unique to Store 2:", store2 - store1)

# 4. Symmetric Difference
print("Symmetric Difference:", store1.symmetric_difference(store2))