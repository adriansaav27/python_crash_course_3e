import privileges as permissions


class Admin(permissions.User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
