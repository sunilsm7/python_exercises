class BestCourse:
    website = "http://cleverprogrammer.com"

    def __init__(self, name):
        self.name = name

course =BestCourse("Learn Python")
learn_command_line_course = BestCourse("learn Command line course")

print(course.name)
print(BestCourse.website)

print(learn_command_line_course.name) #Object_name.method
print(BestCourse.website)  #ClassName.Method
