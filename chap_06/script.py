class Animal:
    name: str = None
    weight: float = None

    def __init__(self, name, weight=None):
        self.name = name
        if weight is not None:
            self.weight = weight

    def speak(self):
        if bool(self.name):
            print(f"I'm {self.name}, an animal")
        else:
            print("I'm an animal")

    def __private_func(self):
        print("Animal")

    def _protected_func(self):
        print("Protected function of Animal class")

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}, {self.weight}"


class Lion(Animal):
    def __init__(self, name, weight=None):
        super().__init__(name, weight)

    def speak(self):
        if bool(self.name):
            print(f"I'm {self.name}, a lion")
        else:
            print("I'm an lion")


class Tiger(Animal):
    def speak(self):
        if bool(self.name):
            print(f"I'm {self.name}, a tiger")
        else:
            print("I'm an tiger")


class Liger(Lion, Tiger):
    """Liger is a real animal
    """

    def __init__(self, name, weight=None):
        super().__init__(name, weight)


animal = Animal("Animal name")
lion = Lion("Simba", 100)
tiger = Tiger("Kitten", 101)
liger = Liger("Liger")

print(animal)  # Animal: Animal name, None
# animal.__private_func()  # AttributeError: 'Animal' object has no attribute '__private_func'
animal._protected_func()  # Protected function of Animal class
animal.speak() # I'm Animal name, an animal
print("--------------------------------")

print(lion) # Lion: Simba, 100
lion.speak() # I'm Simba, a lion
lion._protected_func()  # Protected function of Animal class
print("--------------------------------")

print(tiger) # Tiger: Kitten, 101
tiger.speak() # I'm Kitten, a tiger
print("--------------------------------")

print(liger) # Liger: Liger, None
liger.speak() # I'm Liger, a lion
liger._protected_func()  # Protected function of Animal class
