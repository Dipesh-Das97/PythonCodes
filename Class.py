class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(abc):
        return {
            "name": abc.name,
            "age": abc.age
        }


p1 = Person("Dipesh", 23)
print(p1.my_func())

# A Simple Inheritance:


class Student(Person):
    def print_name(self):
        return "Name is : " + self.name

    def print_age(self):
        return "Age is : " + str(self.age)


p2 = Student("Sahil", 15)
print(p2.print_name())
print(p2.print_age())

# Child class with own constructor:


class Employee(Person):

    def __init__(self, name, age, company, graduated):
        super().__init__(name, age)
        self.graduated = graduated
        self.company = company
        self.team = "Teleport"

    def print_employee_details(self):
        return {
            "name" : self.name,
            "age": self.age,
            "company": self.company,
            "graduated": self.graduated,
            "team": self.team
        }


p3 = Employee("Dipesh Das", 23, "Full", True)
print(p3.print_employee_details())
