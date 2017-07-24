# 1. __init__ ex


class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

kitty = Student('kitty', 85, 25)
daniel = Student('Daniel', 80, 22)

print(kitty.name, kitty.grade, kitty.age)
print(daniel.name, daniel.grade)

