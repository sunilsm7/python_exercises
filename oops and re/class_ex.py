class Person:
    age = 18
    def name(self, name):
        return list(name)

jack = Person()
jack.name = 'Jack Roberts'
jack.age = 16
print(jack.age)
print(jack.name)

bob = Person()
bob.name = "Bob Smith"
print(bob.name)
print(bob.age )
