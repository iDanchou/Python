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


class Developer(Employee):  # inherits all attributes and methods from the employee class
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # better for single inheritance
        # Employee.__init__(self, first, last, pay)  # better for multiple inheritance
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employees(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employees(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print("-->", employee.full_name())


dev_1 = Developer("Sheen", "Kirkland", 50000, "Python")  # 10% instead of 4% because it's taking raise_amount from Developer Class
dev_2 = Developer("Test", "User", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

# print(mgr_1.email)

mgr_1.add_employees(dev_2)
mgr_1.print_employees()

# mgr_1.remove_employees(dev_1)


# print(dev_1.email)
# print(dev_2.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Manager))
