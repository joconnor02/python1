class Bird:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        swag = input("What should " + self.name + " say?")
        print(self.name + " says " + swag)

    def set_species(self):
        money = input("What species is this bird?")
        self.species = money

    def set_name(self):
        baller = input("What is the bird's name?")
        self.name = baller

    def toString(self):
        print("The birds name is " + self.name)
        print("The birds species is " + self.species)
        print("The birds age is " + str(self.age))

b1 = Bird("", "", 0)
b1.set_name()
b1.set_species()

b2 = Bird("", "", 0)
b2.set_name()
b2.set_species()

b1.toString()
b2.toString()
