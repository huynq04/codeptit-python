from math import gcd

for _ in range(int(input())):
    a = int(input())
    b = int(str(a)[::-1])
    if gcd(a, b) == 1:
        print("YES")
    else: print("NO")
