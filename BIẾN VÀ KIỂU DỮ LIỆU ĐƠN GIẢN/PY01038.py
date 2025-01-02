def solve(n):
    res = 0
    if n % 7 == 0:
        return n
    
    for _ in range(1000):
        res = n + int(str(n)[::-1])
        if res % 7 == 0: return res
        n = res
    
    return -1

for _ in range(int(input())):
    print(solve(int(input())))