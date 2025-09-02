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
class PremiumUser(RegisteredUser):
    def __init__(self, username, userId, password, age, subscription_expiration):
        super().__init__(username, userId, password, age)
        self.subscription_expiration = subscription_expiration

    def display_user_info(self):
        base_info = super().display_user_info()
        return (f"{base_info}\n"
                f"Subscription Expiration: {self.subscription_expiration}")
class NonPremiumUser(RegisteredUser):
    def __init__(self, username, userId, password, age):
        super().__init__(username, userId, password, age)

    def display_user_info(self):
        base_info = super().display_user_info()
        return f"{base_info}\nStatus: Non-Premium"
# Example usage
if __name__ == "__main__":
    users = [
        PremiumUser("john_doe", "12345", "securepassword", 30, "2025-05-01"),
        NonPremiumUser("jane_doe", "67890", "anotherpassword", 25)
    ]

    for user in users:
        print(user.display_user_info())
        print()
 
