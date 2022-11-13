import math
class Line:
    def __init__(self,coor1,coor2):
        self.x1,self.y1 = coor1
        self.x2,self.y2 = coor2
    
    def distance(self):
        #d = sqrt(x2-x1 square - y2-y1 square)
        return math.sqrt(math.pow((self.x2 - self.x1),2) + math.pow((self.y2 - self.y1),2))
    
    def slope(self):
        #m = y2-y1/x2-x1
        return (self.y2 - self.y1) / (self.x2 - self.x1)
		
		
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()

li.slope()