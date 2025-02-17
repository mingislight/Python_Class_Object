# Validate Attribute values - Minimum Wages 1000

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)

    def increse_salary(self, percent):
        self.salary += self.salary * (percent/100)

    def __str__(self): # Define the str() method
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}."

    def __repr__(self): # Define the repr() method
        return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"
        
    def get_salary(self):
        # return f"${self.salary}"
        # return f"${self.salary, 2}"  - decimal 2 
        return self.salary
    
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Value Minimum is $1000.')
        self.salary = salary

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

employee1.set_salary(900)
print(employee1.get_salary())