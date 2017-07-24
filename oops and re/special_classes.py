class Animal:
    def __init__(self, name, species):
        print("This came from the init() method")
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __del__(self):
        print("This came from the del() method")

class Fourlegs:
    def hasLegs(self):
        return 4

class Dog(Animal, Fourlegs):
    def __init__(self, name, isBig):
        Animal.__init__(self, name, "Dog")
        self.isBig = isBig
    
    def getName(self): //overridden method
        return self.name, self.species, self.isBig
    