class SV:
    def __init__(self, ten, arr):
        self.ten = ten
        self.bai, self.sub = [int(i) for i in arr.split()]
    
    def __str__(self):
        return f'{self.ten} {self.bai} {self.sub}'

arr = []
for _ in range(int(input())):
    arr.append(SV(input(), input()))

arr.sort(key=lambda e: (-e.bai, e.sub, e.ten))
print(*arr, sep='\n')
        