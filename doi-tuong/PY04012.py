class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop
    
    def cal(self, s):
        m = s.count('m')
        v = s.count('v')
        self.diem = max(0, 10 - m - v*2)
    
    def __str__(self):
        if self.diem != 0:
            return f'{self.ma} {self.ten} {self.lop} {self.diem}'
        return f'{self.ma} {self.ten} {self.lop} {self.diem} KDDK'
    
a = {}
n = int(input())
for i in range(n):
    sv = SinhVien(input(), input(), input())
    a[sv.ma] = sv

for i in range(n):
    ma, s = input().split()
    a[ma].cal(s)

for i in a:
    print(a[i])
        