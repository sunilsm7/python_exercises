# 2. class vs objects

class Fighters:

    def __init__(self, name):
        self.name =name

sunil = Fighters("Sunil")
bob = Fighters("Bob the Builder")
# print(sunil.name)
# print(bob.name)


"""
    Own class
"""
class Racing:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getName(self):
        return self.name

    def getPostion(self):
        return self.position

sm = Racing("sunil", 3)
aj = Racing("Ajay", 2)
vh = Racing('Vishal', 1)

print(sm.getName(), sm.getPostion())