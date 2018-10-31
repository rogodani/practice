'''
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
'''

from math import sqrt, pow


class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return sqrt(pow((self.coor2[0] - self.coor1[0]), 2) + pow((self.coor2[1] - self.coor1[1]), 2))

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())
