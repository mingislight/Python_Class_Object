class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary  # Use property setter

    @property  # Getter for salary
    def salary(self):
        return self._salary

    @salary.setter  # Setter for salary
    def salary(self, value):
        if value < 1000:
            raise ValueError('Value Minimum is $1000.')
        self._salary = value  # Use self._salary to store the value, _salary is private

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
print(employee1.salary)
