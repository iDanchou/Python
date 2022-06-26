class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # allows you to access as an attribute (without additional parenthesis)
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @full_name.setter  # (can only set as name of property) allows you to set a new value
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter  # (can only set as name of property) allows you to delete a value
    def full_name(self):
        print("Deleted Name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")
emp_2 = Employee("John", "Smith")

# emp_1.first = "Jim"
emp_1.full_name = "Sheen Kirkland"

print(emp_1.first)
print(emp_1.email)
# print(emp_1.email())  # to still use email after a name change without property decorator
print(emp_1.full_name)
print(emp_2.full_name)

del emp_2.full_name
