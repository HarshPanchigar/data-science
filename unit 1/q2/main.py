from attendance import *

attendance = [85, 90, 75, 60, 95, 80, 70, 88, 92, 65, 78, 84, 55, 98, 72]

print("Attendance Percentage (40 out of 50):",
    calculate_percentage(40, 50), "%")

# Students having attendance below 75%
print("Students with attendance below 75%:",
      identify(attendance))

# Average attendance
print("Average Attendance:",
      round(average(attendance), 2), "%")