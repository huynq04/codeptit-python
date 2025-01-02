from decimal import Decimal
from math import sqrt, pow

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def distance(self, o):
        tmp = sqrt(pow(self.a - o.a, 2) + pow(self.b - o.b, 2))
        return f'{tmp:.4f}'


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1