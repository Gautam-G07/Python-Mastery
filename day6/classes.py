class Temp:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y
    def peri(self):
        return 2*(self.x+self.y)
obj1=Temp(10,20)
Area=obj1.area()
peri=obj1.peri()
print("Area:",Area)
print("Perimeter:",peri)