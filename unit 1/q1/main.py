from healthutils import *

readings = [120, 145, 135, 160, 118, 142, 130, 155, 125, 148, 138, 110, 170, 140, 150]

print("Blood Pressure Readings:", readings)
print("Highest Blood Pressure:", high_bp(readings))
print("Lowest Blood Pressure:", low_bp(readings))
print("Average Blood Pressure:", average(readings))
print("Patients with BP greater than 140:", count(readings))