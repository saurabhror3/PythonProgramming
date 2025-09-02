class RegisteredUser:
    def __init__(self, username, userId, password, age):
        self.__username = username
        self.__userId = userId
        self.age = age

    def get_username(self):
        return self.__username

    def get_userId(self):
        return self.__userId

    def set_username(self, username):
        if username:  # Simple validation
            self.__username = username
        else:
            raise ValueError("Username cannot be empty")

    def set_userId(self, userId):
        if userId:  # Simple validation
            self.__userId = userId
        else:
            raise ValueError("User ID cannot be empty")
    def display_user_info(self):
        return (f"Username: {self.__username}\n"
                f"User ID: {self.__userId}\n"
            f"Age: {self.age}")
# Example usage
user = RegisteredUser("john_doe", "12345", "securepassword", 30)
print(user.display_user_info())

# Accessing private attributes through getter methods
print(user.age)
print(user.__username)  #Throws error
print(user.get_username())
