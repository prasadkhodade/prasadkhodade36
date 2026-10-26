import json

with open("students.json", "r") as file:
    data = json.load(file)

new_record = {"RollNo": 104, "Name": "David", "Marks": 78}
data.append(new_record)

with open("updated_students.json", "w") as file:
    json.dump(data, file, indent=4)

print("New record added successfully!")
print("Updated data saved to updated_students.json")