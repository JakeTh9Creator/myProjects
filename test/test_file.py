import sys

print(sys.executable)
print(sys.version)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


for num in [1, 2, 3, 4]:
    print(num)

emp_1 = Employee("Mike", "Ainsel")
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
