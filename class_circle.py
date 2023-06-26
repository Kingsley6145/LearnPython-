import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.142 * self.radius**2
        return area

# Creating an object of the Circle class
circle = Circle(7)

# Accessing the radius attribute and calling the calculate_area method
print("Radius:", circle.radius)
print("Area:", circle.calculate_area())
