from student import Student
from file_handler import load_students, save_students

def add_student(student):
  data = load_students()
  # Prevent duplicate roll_no
  if any(s['roll_no'] == student.roll_no for s in data):
    raise ValueError("Roll number already exists.")
  data.append(student.to_dict())
save_students(data)

def get_all_students():
  data = load_students()
  return [Student.from_dict(d) for d in data]

def find_student(roll_no):
  data = load_students()
  for d in data:
    if d['roll_no'] == roll_no:
      return Student.from_dict(d)
  return None

def update_student(roll_no, **kwargs):
  data = load_students()
  for i, d in enumerate(data):
    if d['roll_no'] == roll_no:
      # Update fields if present in kwargs
      for key, value in kwargs.items():
        if key in d:
          d[key] = value
      data[i] = d
      save_students(data)
      return True
  return False

def delete_student(roll_no):
  data = load_students()
  new_data = [d for d in data if d['roll_no'] != roll_no]
  if len(new_data) == len(data):
    return False  # Not found
  save_students(new_data)
  return True
