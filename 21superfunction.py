#superfunction() = used to give access to the method of the parent class
#           returns a temporary object of the parent class when used.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


class Square(Rectangle):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)

    def area(self):
        print("The area of the square : ", end="")
        return self.length*self.breadth


class Cube(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height
    def volume(self):
        print("The volume of the cube : ", end="")
        return self.length*self.breadth*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)
print(square.area())
print(cube.volume())