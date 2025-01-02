from math import gcd


a, b = [int(i) for i in input().split()]

uc = gcd(a, b)

print(f'{int(a/uc)}/{int(b/uc)}')