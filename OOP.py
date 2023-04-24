class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, gender, major):
        super().__init__(name, age, gender)
        self.major = major

    def study(self):
        print(f"I'm a student of {self.major}.")

student1 = Student("Abdi", 19, "Male", "Informatics Engineering")
student1.greet() 
student1.study()
