# 1. Create an empty dictionary to store student records
student_records = {}

while True:
    name = input("Enter student name (or type 'done' to finish): ")
    
    if name.lower() == 'done':
        break

    # 2. Enter subjects (as a comma-separated list)
    subjects_input = input(f"Enter subjects for {name} (comma-separated): ")
    subjects = [subject.strip() for subject in subjects_input.split(",")]

    # 2. Enter grades (as a comma-separated list)
    grades_input = input(f"Enter grades for {name} (comma-separated): ")
    grades = {int(grade.strip()) for grade in grades_input.split(",")}

    # 3. Store the record as a tuple (list of subjects, set of grades)
    student_records[name] = (subjects, grades)

# 4. Display all student records
print("\nStudent Records:")
for student, (subjects, grades) in student_records.items():
    print(f"\nStudent: {student}")
    print("Subjects:", ", ".join(subjects))
    print("Grades:", ", ".join(str(grade) for grade in grades))
