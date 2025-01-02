class Rectangle:
    def __init__(self, d, r, m):
        self.perimeter = (d+r)*2
        self.area = d * r
        self.color = m.title()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter, r.area, r.color))
else: 
    print('INVALID')