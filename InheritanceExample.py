from java.lang import Math

class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, a, b , c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


    def area(self):
        S = self.perimeter()/ 2
        return Math.sqrt(S*(S-self.a)*(S-self.b)*(S-self.c))


    def __repr__(self):
        return "Triangle({0},{1},{2})".format(
            self.a, self.b, self.c
        )


class Rectangle(Shape):
    def __init__(self, width , height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2*(self.width + self.height)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "Rectangle({0},{1})".format(self.width , self.height)


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * Math.PI *self.r

    def area(self):
        return Math.PI* Math.pow(self.r , 2)

    def __repr__(self):
        return "Circle({0})".format(self.r)