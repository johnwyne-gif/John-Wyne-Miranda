class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I study {self.course}.")

student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 22, "Mathematics")
student3 = Student("Charlie", 21, "Physics")

student1.introduce()
student2.introduce()
student3.introduce()
