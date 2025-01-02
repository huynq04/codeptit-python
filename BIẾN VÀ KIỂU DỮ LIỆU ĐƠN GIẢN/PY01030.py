from math import pow, gcd

n, k = [int(i) for i in input().split()]

cnt = 0

for i in range(int(pow(10, k-1)), int(pow(10, k))):
    if gcd(n, i) == 1:
        cnt += 1
        print(i, end=' ')
        if cnt % 10 == 0:
            print()
            