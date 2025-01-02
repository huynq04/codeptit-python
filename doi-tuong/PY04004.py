from math import gcd


a, b, c, d = [int(i) for i in input().split()]

tu = a*d + c*b
mau = b*d

print(f'{tu//gcd(tu, mau)}/{mau//gcd(tu, mau)}')