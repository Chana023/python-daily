# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        result_x = self.x - no.x
        result_y = self.y - no.y
        result_z = self.z - no.z
        return (Points(result_x, result_y, result_z))

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        result_x = self.y * no.z - self.z * no.y 
        result_y =  self.z * no.x - self.x * no.z
        result_z = self.x * no.y - self.y * no.x


        return Points(result_x , result_y, result_z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
  
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))