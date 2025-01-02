from math import sqrt


def nt(n):
    if n < 2: return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n %i==0: return 0
    return 1

n, m = input().split()

for i in range(int(n)):
    a = [nt(int(i)) for i in input().split()]
    print(*a)