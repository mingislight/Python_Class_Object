from dataclasses import dataclass

# pip install mypy 
# mypy program.py  - check type hints

@dataclass(slots=True)
class Project:
    name: str    # Type Hints (data type)
    payment: int # Type Hints (data type)
    client: str  # Type Hints (data type)

    def notify_client(self):
        print(f"Notifying the client about the progress of the {self.name}...")

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)

print(e.project)