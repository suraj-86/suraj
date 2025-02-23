# define a circle class to create a circle with radius r using the constructor.
# define area() method of circle which calculates area .
# define a parimeter( method of circle which calculates parimeter.

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        area=((22/7)*self.radius*self.radius)
        print("area is ",area)

    def parimeter(self):
        parimeter=(2*(22/7)*self.radius)
        print("parimeter is ",parimeter)

c1=Circle(int(input("enter radius : ")))
c1.area()
c1.parimeter()
