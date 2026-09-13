# @property = Decorator that allows you to define a method as a property of a class. 
# This means that you can access the method like an attribute, without needing to call it with parentheses. 
# Benefit of using @property is that it allows you to create read-only attributes, which can help to enforce encapsulation and prevent unintended modifications to the object's state.
# Gives you getter, setter and deleter methods for a class attribute, allowing you to control access to the attribute and enforce any necessary validation or constraints.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # it is intended to be a private attribute, and should not be accessed directly from outside the class.
        
    @property
    def width(self):
        return f"{self._width:.1f}"

    @width.setter
    def width(self, new_width):
        if new_width < 0:
            raise ValueError("Width must be a positive value")
        self._width = new_width

    @property
    def height(self):
        return f"{self._height:.1f}"

    @height.setter
    def height(self, new_height):
        if new_height < 0:
            raise ValueError("Height must be a positive value")
        self._height = new_height

    # @property
    # def area(self):
    #     return self._width * self._height

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(5, 10)
print(rectangle._width)  # Output: 5 - it gives warning that it is a private attribute and should not be accessed directly from outside the class.

rectangle.width = 0
rectangle.height = 12

del rectangle.width  # it will give error as we have not defined deleter method for width
del rectangle.height  # it will give error as we have not defined deleter method for height

# print(rectangle.width)  # Output: 5.0
# print(rectangle.height)  # Output: 10.0 - uncomment the deleter method to see the output of width and height after deletion