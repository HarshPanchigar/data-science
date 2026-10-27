ISBN = (978013, 978024, 978032, 978045, 978056,
    978067, 978078, 978089, 978091, 978102,
    978113, 978124, 978135, 978146, 978157)

# Display all ISBN numbers.
for i in range(len(ISBN)):
    print(i,"-",ISBN[i])

print("\n")
print(ISBN[5])

num = int(input("Enter No: "))
if num in ISBN:
    print("yes")
    print(ISBN.index(num))
else:
    print("Not Found")