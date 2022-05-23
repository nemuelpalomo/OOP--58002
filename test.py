class Shape:
    def square(self):
        return "4 sides are equal"

    def rectangle(self):
        return "2 sides are equal"
class Polygon(Shape):

    def triangle(self):
        return "3 sides"



object = Polygon()

object.square()