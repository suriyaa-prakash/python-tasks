import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def aera(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
r=int(input("Enter radius of circle:"))
c=circle(r)
print("Aera of circle:",round(c.aera(),2))
print("perimeter of the circle:",round(c.perimeter(),2))
