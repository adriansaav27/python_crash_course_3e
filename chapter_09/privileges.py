class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")

    def greet_user(self):
        print(f"Hi {self.first_name}, you're welcome :)")


# admin = Admin("admin", "administrator", 0)
# admin.privileges.show_privileges()
