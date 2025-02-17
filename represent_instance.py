class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increse_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self): # Define the str() method
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}."

    def __repr__(self): # Define the repr() method
        return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"
        

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)
print(str(employee1))
print(repr(employee1))