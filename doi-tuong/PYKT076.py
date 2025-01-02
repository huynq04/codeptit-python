from datetime import datetime


class LoaiPhim:
    def __init__(self, ma, ten):
        self.ma = 'TL{:03}'.format(ma)
        self.ten = ten
    
class Phim:
    def __init__(self, ma, loai, ngay, ten, tap):
        self.ma = 'P{:03}'.format(ma)
        self.loai = loai
        self.ngay = datetime.strptime(ngay, '%d/%m/%Y').date()
        self.strdate = ngay
        self.ten = ten
        self.tap = tap

    def __str__(self):
        return f'{self.ma} {self.loai.ten} {self.strdate} {self.ten} {self.tap}'
    

arr = []
a={}
n, m = [int(i) for i in input().split()]
for _ in range(n):
    loai = LoaiPhim(_+1, input())
    a[loai.ma] = loai
for i in range(m):
    arr.append(Phim(i+1, a[input()], input(), input(), int(input())))

arr.sort(key=lambda e: (e.ngay, e.ten, -e.tap))
print(*arr, sep='\n')