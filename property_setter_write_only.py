# Setter for Write-Only

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary  # Use property setter

    @property  # Getter for salary
    def salary(self):
        raise AttributeError("Salary is write-only.")

    @salary.setter  # Setter for salary
    def salary(self, value):
        self._salary = value

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def __str__(self):  # Define the str() method
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}."

    def __repr__(self):  # Define the repr() method
        return f"Employee({self.name}, {self.age}, {self.position}, {self.salary})"

# Create employee instances
employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

# Set new salary using the setter
employee1.salary = 2000

# Print salary
print(employee1._salary)  # Stored Encripted Salary Mount
