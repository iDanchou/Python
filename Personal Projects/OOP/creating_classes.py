class Employee:  # defining a class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee("Sheen", "Kirkland", 50000)  # The same as code below but shorthanded
# emp_1.first = "Sheen"
# emp_1.last = "Kirkland"
# emp_1.email = "Sheen.Kirkland@company.com"
# emp_1.pay = 50000

emp_2 = Employee("Test", "User", 60000)

print(emp_1.email)
print(emp_2.pay)

print(emp_1.full_name())  # Won't need to pass self for instance because it is added automatically
print(Employee.full_name(emp_1))  # When calling from class will need to add instance


