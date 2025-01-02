from math import sqrt

def nt(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n%i==0: return False
    return True

def solve(s):
    if not nt(len(s)):
        return 'NO'
    cnt = 0
    for i in s:
        if nt(int(i)):
            cnt+=1
    if cnt <= len(s) - cnt:
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    s = input()
    print(solve(s))
