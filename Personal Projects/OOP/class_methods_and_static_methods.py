import datetime


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

    @classmethod  # alters functionality of the method
    def set_raise_amount(cls, amount):  # receives class(cls) rather than instance(self) as parameter
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay)

    @staticmethod  # doesn't take class or instance as a parameter and acts as a normal function
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # uses the weekday method to check where day falls 0-6 Mon-Sun
            return False
        return True


emp_1 = Employee("Sheen", "Kirkland", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_string_1 = "John-Doe-70000"
emp_string_2 = "Steve-Smith-30000"
emp_string_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_string_1)  # passes in string to parse with class method and create new employee

Employee.set_raise_amount(1.05)  # Automatically works within Employee class to update raise_amount variable
# Employee.raise_amount = 1.05  # Same as code above

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

my_date = datetime.date(2022, 6, 25)
print(Employee.is_workday(my_date))
