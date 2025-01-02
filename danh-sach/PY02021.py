from collections import Counter


for _ in range(int(input())):
    n, m, k = input().split()

    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]

    counter_a = Counter(a)
    counter_b = Counter(b)
    counter_c = Counter(c)

    giao = counter_a & counter_b & counter_c

    if len(giao) == 0:
        print('NO')
    else:
        for i in giao.elements():
            print(i, end=' ')
    print()

