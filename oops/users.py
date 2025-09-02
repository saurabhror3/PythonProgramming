class RegisteredUser:

  def __init__(self, username, userId, password, age):
    self.username = username
    self.userId = userId
    self.password = password
    self.age = age

  def display_user_info(self):
    return (f"Username: {self.username}\n"
            f"User ID: {self.userId}\n"
            f"Age: {self.age}")


if __name__ == "__main__":
  user = RegisteredUser("john_doe", "12345", "securepassword", 30)
  print(user.display_user_info())
