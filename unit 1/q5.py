aqi = [85, 220, 95, 160, 75, 210, 130, 180, 65, 145, 110, 200, 90, 155, 100]

count = 0
for i in aqi:
    if i > 200:
        count += 1
print("AQI greater than 200 : ", count,"\n")

# Categorize AQI as Good, Moderate, Poor, or Very Poor. 
for i in aqi:
    if i <= 50:
        category = "Good"
    elif i <= 100:
        category = "Moderate"
    elif i <= 200:
        category = "Poor"
    else:
        category = "Very Poor"

    print(i , "-" , category)

print(sorted(aqi))
print(sorted(aqi,reverse=True))