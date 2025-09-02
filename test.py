# class Student:
#   def __init__(self, low, high):
#     self.low = low;
#     self.high = high;

#   def counter(self):
#     arr = []
#     for i in range(self.low, self.high):
#       arr.append(i)
#     return arr

# std = Student(1, 10)

# print(std.counter())


# class Student:
#   def __init__(self,low,high):
#     self.low = low
#     self.high = high

  # def __iter__(self):
  #   return self

#   def __next__(self):
#     if self.low > 7:
#       raise StopIteration
#     else:
#       current = self.low
#       self.low +=1
#       return current

# for num in Student(1,10):
#   print(num)


class Student:
  def __init__(self, low, high):
    self.low = low
    self.high = high

  def __iter__(self):
    return self

  def count_num(n):
    i = 1
    while i <= n:
      yield i
      i += 1

for num in Student(1, 5):
  print(num)


