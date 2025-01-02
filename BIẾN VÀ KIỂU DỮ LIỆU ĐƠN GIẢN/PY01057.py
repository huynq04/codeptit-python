from math import sqrt

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i==0:
            return False
        
    return True

def solve(n):
    for i in range(len(n)):
        if nt(i) and not nt(int(n[i])):
            return 'NO'
        if not nt(i) and nt(int(n[i])):
            return 'NO'
        
    return 'YES'

for _ in range(int(input())):
    s = input()
    print(solve(s))
