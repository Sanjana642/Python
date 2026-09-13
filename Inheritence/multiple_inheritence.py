# multiple inheritence = inherit from more than one parent class- C(A,B)

# multi-level inheritence = inherit from parent which inherits from another parent- 
#                            C(B) <- B(A) <- A

class Animal:   # Grand-parent  

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):  # Parent
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):  # Parent 
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):   # Child
    pass

class Hawk(Predator):      # Child
    pass

class Fish(Prey, Predator):    # Child
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Poco")

rabbit.eat()  # This animal is eating
fish.sleep()  # This animal is eating
# output - Bugs is eating (after __init__ method)
#  Poco is sleeping

hawk.sleep()    # Tony is sleeping
hawk.hunt()   # Tony is hunting