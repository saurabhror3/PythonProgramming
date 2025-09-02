import math

# 1. Base class: Shape
class Shape:
    def __init__(self, color):
        self.__color = color  # Encapsulated attribute

    def get_color(self):
        return self.__color

    def area(self):
        return 0  # Base class doesn't define area

    def __str__(self):
        return f"A shape with color {self.__color}"


# 2. Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"Rectangle (Color: {self.get_color()}, Width: {self.__width}, Height: {self.__height})"


# 3. Derived class: Circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __str__(self):
        return f"Circle (Color: {self.get_color()}, Radius: {self.__radius})"


# 4. Demonstrate Polymorphism
shapes = [
    Rectangle("Red", 4, 6),
    Circle("Blue", 3),
    Rectangle("Green", 2.5, 3.5),
    Circle("Yellow", 1.2)
]

# Iterate through the shapes and print descriptions and areas
for shape in shapes:
    print(shape)                  # Uses __str__() from the derived class
    print(f"Area: {shape.area():.2f}\n")  # Polymorphic call to area()
