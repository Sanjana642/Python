# super() = Function used in child class to call methods from parent class (superclass)
#           Allows you to extend the functionality of the inherited methods 

class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  #instead of super() you can use Shape(parent class)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        # here parent and child method (describe) is same so it will use first childs method
        super().describe()
        # here we are extending functionality
        print("--------------")


class Square(Shapes):
    def __init__(self, color, is_filled,  width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()
        print("--------------")

class Triangle(Shapes):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is Triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()

circle = Circle(color="blue", is_filled=True, radius=5)
square = Square(color="crimsom", is_filled=False, width=10)
triangle = Triangle(color="green",is_filled=True, width=8, height=8)

print(circle.color)     #blue
print(circle.is_filled)  # True
print(circle.radius)    # 5

print(square.color)  #crimson 
print(square.is_filled) # False
print(f"{square.width}cm")   # 10cm

print(triangle.color)   # green
print(triangle.is_filled)  # True
print(f"{triangle.width}cm")  #8cm
print(f"{triangle.height}cm")  #8cm

circle.describe()   # It is blue and filled
square.describe()   # It is crimsom and not filled
triangle.describe() # It is green and filled

# after adding describe and super() to each shape the output is-
# It is a circle with an area of 78.5cm^2
# It is blue and filled
# --------------
# It is a square with an area of 100cm^2
# It is crimsom and not filled
# --------------
# It is Triangle with an area of 32.0cm^2
# It is green and filled