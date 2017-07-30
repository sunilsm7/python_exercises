class Animal():
    name = 'Amy'
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = 'Covers body'
    def get_color(self, abc):
        return self.color + " " + abc
    @property
    def make_noise(self):
        return self.noise
    def get_size(self):
        return self.size



dog = Animal()
print(dog.get_color("red"))
print(dog.get_size())
print(dog.make_noise)
