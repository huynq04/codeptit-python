from collections import Counter
from math import sqrt


def nt(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i==0: return False
    return n >=2

n = input()
a = Counter([int(i) for i in input().split()]).items()

for k, v in a:
    if nt(k):
        print(f'{k} {v}')