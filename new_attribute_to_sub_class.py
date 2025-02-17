class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary  
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Tester(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework   # Adding new attrivutes to sub class

    def run_tests(self):
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")
    
class Developer(Employee):
    def increase_salary(self, percent, bonus):
        super().increase_salary(percent)     # Employee.increase_salary(self, percent); can't use self, for the child class looping itself
        self.salary += bonus

employee1 = Tester("Lauren", 44, 1000, "Flask")
employee2 = Developer("Ji-Soo", 38, 1000)

employee1.increase_salary(20)      # increase_salary() inherited from super class
employee2.increase_salary(20, 30)  # increase_salary)() inherited from sub class

print(employee1.framework)