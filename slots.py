# SLOTS:
#  1. Faster Attribute Access 2. Reduced Memory Overhead

class Developer:
    __slots__ = ("name", "age", "salary", "framework") # Store slots in instances

    def __init__(self, name, age, salary, framework):
        self.name = name
        self.age = age
        self.salary = salary  
        self.framework = framework

employee1 = Developer("Ji-Soo", 38, 1000, "Flask")

print(employee1.__slots__)