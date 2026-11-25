class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
r=Rectangle(4,3)
print(r.width * r.height)
        
a = Rectangle(2, 5)
b = Rectangle(3, 3)
a.width = 10
print(a.width, b.width)

