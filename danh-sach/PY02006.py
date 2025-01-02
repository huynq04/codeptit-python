def solve(a, b):
    for i in range(n):
        if a[i] > b[i]:
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    n = int(input())
    a, b = [int(i) for i in input().split()], [int(i) for i in input().split()]
    print(solve(sorted(a), sorted(b)))
