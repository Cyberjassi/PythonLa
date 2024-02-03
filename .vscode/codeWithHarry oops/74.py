class area:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y
class circle(area):
    def area(self):
        return super().area()*self.x
    
s = circle(2,3)
print(s.area())
    