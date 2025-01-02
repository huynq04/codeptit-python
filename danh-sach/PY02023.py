for t in range(int(input())):
    n = int(input())
    a = input().split()
    a.sort(key=lambda e: (sum(int(i) for i in e), int(e)))
    print(*a)