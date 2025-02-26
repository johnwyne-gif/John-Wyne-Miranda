class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"New salary for {self.name} after raise: ${self.salary}")

    def display_employee(self):
        print(f"Employee Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")

employee = Employee("Jane Smith", "Software Engineer", 70000)
employee.display_employee()
employee.give_raise(5000)
employee.display_employee()
