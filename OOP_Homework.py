'''
Homework Assignment
Problem 1

Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
In [1]:

class Line:

    def __init__(self,coor1,coor2):
        pass

    def distance(self):
        pass

    def slope(self):
        pass

In [2]:

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
'''


class Line:

    def __init__(self, coor1, coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2+(y2-y1)**2)**.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)
coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())