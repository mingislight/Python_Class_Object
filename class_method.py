from datetime import date

class Employee:
    minimum_wage = 1000

    @classmethod        
    def change_minimum_wage(cls, new_wage):     #Update class methods
        if new_wage > 3000:
            raise ValueError("Company is bankrupt.")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

e = Employee.new_employee("Mary", date(1991, 8, 12))
print(e.name)
print(e.age)
print(e.salary)