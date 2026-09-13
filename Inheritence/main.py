# Inheritence = Allows a class to inherit attributes and methods from another class
#       helps with class reusuability and extensibility
#       class Child (parent)

# class Father:
#     height = "182"
#     color = "pink"

# class Son(Father):
#     pass

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
# Scooby
# True
# Scooby is eating
# Scooby is sleeping  (if cat- Garfield is sleeping) likewise mouse

dog.speak()   # WOOF!