hashtags = [
    "#Python", "#AI", "#Coding", "#Technology", "#Gaming",
    "#Cricket", "#Music", "#Education", "#Travel", "#Fitness",
    "#DataScience", "#MachineLearning", "#Python", "#Trending", "#AI"
]

unique = []
for i in hashtags:
    if i not in unique:
        unique.append(i)

for i in unique:
    print(i,end=" | ")

num = int(input("\nEnter how many new hashtage do you want to add : "))
for i in range(num):
    hashtags.append(input(f"{i+1} - "))

print(hashtags)

count = 0
unique_c = []
for i in hashtags:
    if i not in unique_c:
        unique_c.append(i)
    else:
        count += 1

print(count)