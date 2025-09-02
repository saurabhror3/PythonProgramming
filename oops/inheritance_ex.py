from datetime import date
class RegisteredUser:
    def __init__(self, 
username, userId, password, age):
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
    def has_active_subscription(self):
        today = date.today()
        return today <= self.subscription_expiration

# Subclass for Non-Premium Users
class NonPremiumUser(RegisteredUser):
    def __init__(self, username, userId, 
password, age):
        super().__init__(username, userId, password, age)

    def display_user_info(self):
        base_info = super().display_user_info()
        return f"{base_info}\nStatus: Non-Premium"

if __name__ == "__main__":
    premium_user = PremiumUser("john_doe", "12345", "securepassword", 30, date(2025, 5, 1))
    non_premium_user = NonPremiumUser("jane_doe", "67890", "anotherpassword", 25)

    print("Premium User Info:")
    print(premium_user.display_user_info())
    print(f"Active Subscription: {premium_user.has_active_subscription()}\n")

    print("Non-Premium User Info:")
    print(non_premium_user.display_user_info())
