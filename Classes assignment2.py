import math
class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        # v = self.pi * pow(r,2) * h
        return self.pi * math.pow(self.radius,2) * self.height
    
    def surface_area(self):
        #A=2πrh+2πr2
        return (2 * self.pi * self.radius * self.height) + (2 * self.pi * math.pow(self.radius,2))
		
c = Cylinder(2,3)

c.volume()

c.surface_area()