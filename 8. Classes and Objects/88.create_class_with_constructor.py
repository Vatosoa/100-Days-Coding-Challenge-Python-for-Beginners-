class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rectangle = Rectangle(5,3)
print(f"The area of the rectangle is: {rectangle.area()}")