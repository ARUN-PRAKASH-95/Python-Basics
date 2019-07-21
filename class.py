class Rectangle:
    def __init__(self,length,width):     # init method which contains global attributes of the final object
        self.length = length
        self.width  = width

    def area(self):
        return self.length*self.width
    
    def perimeter(self):
        return 2*(self.length+self.width)

    
# rectangle_1 = Rectangle(length=4, width=3)
# print(rectangle_1.perimeter())
# print(type(rectangle_1))

class Square(Rectangle):
    def __init__(self,a):
        super().__init__(length=a, width=a)
        # self.length = a
        # self.width  = a

square_1 = Square(5)
print('area:',square_1.area())
print(isinstance(square_1,Square))