class Employee:

    def __init__(self, name, last_name, annual_salary):
        self.name = name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, money=5_000):
        self.annual_salary += money
