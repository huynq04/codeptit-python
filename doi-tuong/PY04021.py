class ThoiGian:
    def __init__(self, id, ten, vao, ra):
        self.id = id
        self.ten = ten
        giov, phutv = [int(i) for i in vao.split(':')]
        gior, phutr = [int(i) for i in ra.split(':')]
        self.phut = (gior - giov) * 60 + (phutr - phutv)

    def __str__(self):
        return f'{self.id} {self.ten} {self.phut // 60} gio {self.phut % 60} phut'


arr = []
for _ in range(int(input())):
    arr.append(ThoiGian(input(), input(), input(), input()))

arr.sort(key=lambda e: -e.phut)
print(*arr, sep='\n')


        