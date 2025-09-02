import csv
import json

# Step 1: Create an empty dictionary to store student records
# Format: { "Student Name": (["subjects"], ["grades"]) }
student_records = {}

# Step 2: Prompt the user to enter student data
print("Enter student records. Type 'done' when finished.\n")

while True:
    name = input("Enter student name: ")
    if name.lower() == 'done':
        break

    subjects_input = input("Enter subjects (comma-separated): ")
    grades_input = input("Enter grades (comma-separated): ")

    # Split and clean input
    subjects = [sub.strip() for sub in subjects_input.split(',')]
    grades = [grade.strip() for grade in grades_input.split(',')]

    # Check if subjects and grades match
    if len(subjects) != len(grades):
        print("Error: Number of subjects and grades must match.\n")
        continue

    # Step 3: Store in the dictionary
    student_records[name] = (subjects, grades)

# Step 4: Write to CSV
with open('students.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Subjects', 'Grades'])  # Header

    for name, (subjects, grades) in student_records.items():
        writer.writerow([name, ', '.join(subjects), ', '.join(grades)])

# Step 5: Write to JSON
json_data = {}
for name, (subjects, grades) in student_records.items():
    json_data[name] = {
        'subjects': subjects,
        'grades': grades
    }

with open('students.json', 'w') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)

# Step 6: Read and display both files

print("\nContents of students.csv:")
with open('students.csv', 'r') as csvfile:
    print(csvfile.read())

print("\nContents of students.json:")
with open('students.json', 'r') as jsonfile:
    print(jsonfile.read())
