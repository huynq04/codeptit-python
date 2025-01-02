n, m = input().split()

a = list(set([int(i) for i in input().split()]))
b = list(set([int(i) for i in input().split()]))

if a == b:
    print('YES')
else:
    print('NO')