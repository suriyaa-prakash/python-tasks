class vehicle:
    def twoweeler(self):
        print("2weeler vehicle")
class fourweeler(vehicle):
    def fourweeler(self):
        print("fourweeler vehicle")
v=fourweeler()
v.fourweeler()
v.twoweeler()

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Create a Circle object
circle = Circle(2)

# Calculate and print the area
print("Area:", circle.area())

# Calculate and print the perimeter
print("Perimeter:", circle.perimeter())