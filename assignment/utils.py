def get_int(prompt, min_val=None, max_val=None):
  while True:
    try:
      val = int(input(prompt))
      if min_val is not None and val < min_val:
        print(f"Value must be at least {min_val}.")
        continue
      if max_val is not None and val > max_val:
        print(f"Value must be at most {max_val}.")
        continue
      return val
    except ValueError:
      print("Please enter a valid integer.")

def print_student(student):
  print(f"Name: {student.name}")
  print(f"Roll No: {student.roll_no}")
  print(f"Department: {student.department}")
  print(f"Age: {student.age}")
  print(f"Marks: {student.marks}")
  print(f"Average: {student.average():.2f}")
  print(f"Result: {student.result()}")
  print("-" * 30)
