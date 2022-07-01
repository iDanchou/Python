class Employee:
    raise_amount = 1.04  # Creating a class variable
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_employees += 1  # Better than using self.num_of_employees because we want constant within class

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # can also use Employee.raise_amount but this is recommended


print(Employee.num_of_employees)
emp_1 = Employee("Sheen", "Kirkland", 50000)
emp_2 = Employee("Test", "User", 60000)
print(Employee.num_of_employees)

# print(emp_1.__dict__)  # Will print out all information for Employee 1 in a dictionary
# print(Employee.__dict__)  # Will print out all information for the Employee class

emp_1.raise_amount = 1.05  # Creates and changes emp_1 raise_amount variable for only this employee
# emp_1.apply_raise()  # Will apply raise based on emp_1 current pay rather than the class'

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

