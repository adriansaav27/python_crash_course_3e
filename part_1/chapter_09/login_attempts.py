class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Alvaro", "Palacios", 36)
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login Attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Login Attempts: {user.login_attempts}")
