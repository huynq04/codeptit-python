class Matrix:
    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt
    
    def mul(self):
        res = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                res[i][j] = 0
                for k in range(self.m):
                    res[i][j] += self.mt[i][k]*self.mt[j][k]
        return Matrix(self.n, self.n, res)
        
    def __str__(self):
        for i in self.mt:
            print(*i)
        return ''    

for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    mt = []
    for i in range(n):
        mt.append([int(j) for j in input().split()])
    matrix = Matrix(n, m, mt)
    print(matrix.mul())