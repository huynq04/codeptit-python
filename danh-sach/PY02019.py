from math import gcd


n, a = int(input()), [int(i) for i in input().split()]

a.sort()

for i in range(n):
    for j in range(i+1, n):
        if gcd(a[i], a[j]) == 1:
            print(f'{a[i]} {a[j]}')