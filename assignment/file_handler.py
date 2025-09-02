import json

FILE_NAME = "students.txt"

def load_students():
  try:
    with open(FILE_NAME, "r") as f:
      data = json.load(f)
      return data  # List of dicts
  except (FileNotFoundError, json.JSONDecodeError):
    return []

def save_students(data):
  try:
    with open(FILE_NAME, "w") as f:
      json.dump(data, f, indent=4)
  except Exception as e:
    print(f"Error saving data: {e}")
