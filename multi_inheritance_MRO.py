# Multiple Inheritance 
# Method Resolution Order (MRO), first parameter first, second second

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

class SlotsInspectorMixin:
    def has_slots(self):
        return hasattr(self, "__slots__")

class Developer(SlotsInspectorMixin, Employee):  # MRO: SlotsInspectorMixin → Employee
    __slots__ = ("framework", )

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)  # Calls Employee's increase_salary()
        self.salary += bonus

employee1 = Developer("Ji-Soo", 38, 1000, "Flask")
print(employee1.has_slots())  # Expected: True
print(Developer.__mro__)  # Print Method Resolution Order
