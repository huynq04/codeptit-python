class HoaDon:
    def __init__(self, id, ten, socu, somoi):
        self.id = 'KH{:02}'.format(id)
        self.ten = ten
        self.cnt = somoi - socu

    def cal(self):
        gia = 0
        if self.cnt <= 50:
            gia = self.cnt * 100
            gia *= 1.02
        elif self.cnt <= 100:
            gia = 50 * 100 + (self.cnt - 50) * 150
            gia *= 1.03
        else:
            gia = 50*100 + 50*150 + (self.cnt - 100) * 200
            gia *= 1.05

        return round(gia)
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.cal()}'
    
arr = []
for i in range(int(input())):
    arr.append(HoaDon(i+1, input(), int(input()), int(input())))

arr.sort(key=lambda e: (-e.cal()))
print(*arr, sep='\n')
        