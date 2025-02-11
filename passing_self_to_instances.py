# Obejct: name1.attributes1
# Dictionary: name1['attributes1]

class Employee: 
    def __init__(self, name, age, position, salary): # Parameters: self, (attributes)
        self.name = name  # Passing self to instance
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(employee, percent):
        employee.salary += employee.salary * (percent / 100)

    def info(employee):
        print(f"{employee.name} is {employee.age} years old. Employee is a {employee.position} with the salary of ${employee.salary}.")


employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

Employee.increase_salary(employee2, 20) # Using the dictionary to manage attributes
Employee.info(employee2)

# employee2.increase_salary(20)
# employee2.info()