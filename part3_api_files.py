# ==============================
# PART 3: FILE HANDLING + API
# ==============================

import json
import requests

# ------------------------------
# TASK 1: WRITE DATA TO FILE
# ------------------------------

students = [
    {"name": "Mahi", "marks": [80, 85, 90]},
    {"name": "Rahul", "marks": [60, 70, 65]},
    {"name": "Ananya", "marks": [90, 95, 92]}
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

print("✅ Student data written to file")

# ------------------------------
# TASK 2: READ DATA FROM FILE
# ------------------------------

with open("students.json", "r") as f:
    data = json.load(f)

print("\n📖 Reading Data:")
for student in data:
    avg = sum(student["marks"]) / len(student["marks"])
    print(f"{student['name']} → Average: {round(avg, 2)}")

# ------------------------------
# TASK 3: MODIFY DATA
# ------------------------------

for student in data:
    student["status"] = "Pass" if sum(student["marks"]) / len(student["marks"]) >= 60 else "Fail"

with open("students_updated.json", "w") as f:
    json.dump(data, f, indent=4)

print("\n✏️ Updated data saved")

# ------------------------------
# TASK 4: API CALL
# ------------------------------

print("\n🌐 Fetching Data from API...")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    print("\n👥 API Users (First 3):")
    for user in users[:3]:
        print(f"{user['name']} - {user['email']}")
else:
    print("❌ Failed to fetch API data")