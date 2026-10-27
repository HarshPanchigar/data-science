datasets = [
    ("Student Data", 500, 10),
    ("Sales Data", 1200, 8),
    ("Employee Data", 300, 12),
    ("Weather Data", 2500, 6),
    ("Health Data", 800, 15),
    ("Movie Data", 1500, 9),
    ("Customer Data", 2000, 11),
    ("Product Data", 950, 7),
    ("Traffic Data", 3000, 14),
    ("Bank Data", 1800, 13),
    ("Housing Data", 600, 10),
    ("Sports Data", 1100, 8),
    ("Crime Data", 2200, 12),
    ("Education Data", 750, 9),
    ("Sensor Data", 4000, 16)
]
print("All Datasets:")

# for i in datasets:
#     print(i)

# Find the dataset having the maximum number of records.
max_number = datasets[0]

for i in datasets:
    if i[1] > max_number[1]:
        max_number = i
print(max_number)

print("With Lamda")
max_data = max(datasets,key=lambda x : x[1])
print(max_data)

# Find the dataset having the maximum number of features. 
max_feature = datasets[0]
for i in datasets:
    if i[2] > max_feature[2]:
        max_feature = i
print(max_feature)

print("With Lamda")

mmax_feature = max(datasets , key=lambda x : x[2])
print(mmax_feature)

# Display all dataset names.
for i in datasets:
    print(i[0])