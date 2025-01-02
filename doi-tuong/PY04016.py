from datetime import datetime

gia = {'1': 25, '2': 34, '3': 50, '4': 80}

class DonGia:
    def __init__(self, id, ten, phong, den, di, them):
        self.id = 'KH{:02}'.format(id)
        self.ten = ten
        self.phong = phong
        self.ngayo = (datetime.strptime(di, '%d/%m/%Y') - (datetime.strptime(den, '%d/%m/%Y'))).days + 1
        self.tong = self.ngayo * gia[self.phong[0]] + them

    def __str__(self):
        return f'{self.id} {self.ten} {self.phong} {self.ngayo} {self.tong}'

arr=[]
for i in range(int(input())):
    arr.append(DonGia(i+1, input(), input(), input().strip(), input().strip(), int(input())))

arr.sort(key=lambda e: -e.tong)
print(*arr, sep='\n')