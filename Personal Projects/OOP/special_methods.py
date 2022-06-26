class Employee:
    raise_amount = 1.04  # Creating a class variable
    num_of_employees = 0

    def __init__(self, first, last, pay):  # __init__ (dunder init)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_employees += 1  # Better than using self.num_of_employees because we want constant within class

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # can also use Employee.raise_amount but this is recommended

    def __repr__(self):  # should be used for debugging and logging, easy to copy and paste
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):  # readable display for end user
        return '{} - {}'.format(self.full_name(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee("Sheen", "Kirkland", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1 + emp_2)  # uses __add__ to combine the salary of both employees

# print(emp_1)  # will default to str before repr
print(emp_1.__repr__())
print(emp_1.__str__())

# __add__ can be used for both strings and integers
