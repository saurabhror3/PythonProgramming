from student import Student
import operations as ops
import utils

def main():
  while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = utils.get_int("Enter choice: ", 1, 6)

    if choice == 1:
      name = input("Name: ")
      roll_no = input("Roll No: ")
      department = input("Department: ")
      age = utils.get_int("Age: ", 1)
      marks = []
      for i in range(1, 4):
        mark = utils.get_int(f"Mark {i}: ", 0, 100)
        marks.append(mark)
      try:
        student = Student(name, roll_no, department, age, marks)
        ops.add_student(student)
        print("Student added successfully.")
      except ValueError as e:
        print(e)

    elif choice == 2:
      students = ops.get_all_students()
      if not students:
        print("No student records found.")
      for s in students:
        utils.print_student(s)

    elif choice == 3:
      roll_no = input("Enter Roll No to search: ")
      student = ops.find_student(roll_no)
      if student:
        utils.print_student(student)
      else:
        print("Student not found.")

    elif choice == 4:
      roll_no = input("Enter Roll No to update: ")
      student = ops.find_student(roll_no)
      if not student:
        print("Student not found.")
        continue
      print("Leave field blank to skip updating it.")
      name = input(f"Name [{student.name}]: ") or student.name
      department = input(f"Department [{student.department}]: ") or student.department
      age_input = input(f"Age [{student.age}]: ")
      age = int(age_input) if age_input.strip() else student.age

      marks = []
      for i, m in enumerate(student.marks, start=1):
        mark_input = input(f"Mark {i} [{m}]: ")
        marks.append(int(mark_input) if mark_input.strip() else m)

      updated = ops.update_student(roll_no, name=name, department=department, age=age, marks=marks)
      if updated:
        print("Student updated successfully.")
      else:
        print("Failed to update student.")

    elif choice == 5:
      roll_no = input("Enter Roll No to delete: ")
      deleted = ops.delete_student(roll_no)
      if deleted:
        print("Student deleted successfully.")
      else:
        print("Student not found.")

    elif choice == 6:
      print("Exiting...")
      break

if __name__ == "__main__":
  main()
