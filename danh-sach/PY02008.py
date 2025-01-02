from math import sqrt

def nt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n))+1):
        if n%i==0: return False

    return True

a = [0, 2]
k = 3
while len(a) <= 1000:
    if nt(k):
        a.append(k)
    k+=2

n, x = [int(i) for i in input().split()]

for i in range(n+1):
    x += a[i]
    print(x, end=' ')