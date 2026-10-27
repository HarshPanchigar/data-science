# Nested dictionary of 15 patients
patients = {
    101: {"Name": "Amit", "Age": 25, "Blood Group": "A+", "Disease": "Fever", "Ward": "A"},
    102: {"Name": "Riya", "Age": 30, "Blood Group": "B+", "Disease": "Malaria", "Ward": "B"},
    103: {"Name": "Raj", "Age": 45, "Blood Group": "O+", "Disease": "Diabetes", "Ward": "C"},
    104: {"Name": "Neha", "Age": 22, "Blood Group": "AB+", "Disease": "Flu", "Ward": "A"},
    105: {"Name": "Karan", "Age": 35, "Blood Group": "A+", "Disease": "Asthma", "Ward": "B"},
    106: {"Name": "Priya", "Age": 28, "Blood Group": "O-", "Disease": "Fever", "Ward": "C"},
    107: {"Name": "Rahul", "Age": 50, "Blood Group": "B+", "Disease": "BP", "Ward": "A"},
    108: {"Name": "Pooja", "Age": 40, "Blood Group": "A-", "Disease": "Migraine", "Ward": "B"},
    109: {"Name": "Vijay", "Age": 32, "Blood Group": "O+", "Disease": "Flu", "Ward": "C"},
    110: {"Name": "Anjali", "Age": 27, "Blood Group": "AB+", "Disease": "Fever", "Ward": "A"},
    111: {"Name": "Rohan", "Age": 38, "Blood Group": "B-", "Disease": "Asthma", "Ward": "B"},
    112: {"Name": "Kavya", "Age": 24, "Blood Group": "A+", "Disease": "Flu", "Ward": "C"},
    113: {"Name": "Manav", "Age": 55, "Blood Group": "O+", "Disease": "Diabetes", "Ward": "A"},
    114: {"Name": "Diya", "Age": 29, "Blood Group": "B+", "Disease": "Fever", "Ward": "B"},
    115: {"Name": "Arjun", "Age": 42, "Blood Group": "AB-", "Disease": "BP", "Ward": "C"}
}

# Display patients by blood group
bg = input("\nEnter Blood Group to search: ")
for pid, details in patients.items():
    if details["Blood Group"].lower() == bg.lower():
        print(pid, details)
# Search patient using Patient ID
pid = int(input("Enter Patient ID to search: "))
if pid in patients:
    print("Patient Details:", patients[pid])
else:
    print("Patient not found")

# Update disease
pid = int(input("\nEnter Patient ID to update disease: "))
if pid in patients:
    patients[pid]["Disease"] = input("Enter new disease: ")
    print("Disease updated successfully")
else:
    print("Patient not found")
