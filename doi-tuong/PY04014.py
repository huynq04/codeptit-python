class SinhVien:
    def __init__(self, id, name, total):
        self.id = 'HS{:02}'.format(id)
        self.name = name
        self.avg = round(total / 10 / 1.2, 1)
    
    def TongKet(self):
        if self.avg >= 9:
            return 'XUAT SAC'
        if self.avg >= 8:
            return 'GIOI'
        if self.avg >= 7:
            return 'KHA'
        if self.avg >= 5:
            return 'TB'
        return 'YEU'
        
    def __str__(self):
        return f'{self.id} {self.name} {self.avg} {self.TongKet()}'
    

arr = []

for i in range(int(input())):
    name = input()
    p = [float(i) for i in input().split()]
    tong = sum(p) + p[0] + p[1]
    arr.append(SinhVien(i+1, name, tong))

arr.sort(key=lambda e: (-e.avg, e.id))
for i in arr:
    print(i)
        