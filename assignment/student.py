class Student:
  def __init__(self, name, roll_no, department, age, marks):
    self.name = name
    self.roll_no = roll_no
    self.department = department
    self.age = age
    self.marks = marks  # list of 3 marks

  def average(self):
    return sum(self.marks) / len(self.marks)

  def result(self, pass_mark=35):
    return "Pass" if all(mark >= pass_mark for mark in self.marks) else "Fail"

  def to_dict(self):
    return {
      "name": self.name,
      "roll_no": self.roll_no,
      "department": self.department,
      "age": self.age,
      "marks": self.marks
    }

  @classmethod
  def from_dict(cls, data):
    return cls(
      data["name"],
      data["roll_no"],
      data["department"],
      data["age"],
      data["marks"]
    )
