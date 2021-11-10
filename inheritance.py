class Animal:

    def __init__(self, animal_type, habitat):
        self.animal_type = animal_type
        self.habitat = habitat
        self.food = "plants"

    def who_am_i(self):
        print(f"Hello, I'm {self.animal_type} and I live on {self.habitat}.")


class Dog(Animal):
    sound = "waf waf"

    def __init__(self, breed, color):
        super().__init__("mammal", "ground")
        self.breed = breed
        self.color = color

    def who_am_i(self):
        print("I'm a dog")
        super().who_am_i()

    def make_sound(self):
        print(self.sound)


class Cat(Animal):
    sound = "mjau mjau"

    def __init__(self, breed, color):
        super().__init__("mammal", "ground")
        self.breed = breed
        self.color = color
        self.food = "meat"

    def make_sound(self):
        print(self.sound)


class Labrador(Dog):
    pass


johnny = Dog("labrador", "black")
print(johnny.food)
johnny.who_am_i()

my_cat = Cat("bombai", "black")
my_cat.who_am_i()
my_cat.make_sound()