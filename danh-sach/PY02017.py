from collections import Counter


for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    cnt_a = Counter(a).items()
    for k, v in cnt_a:
        if v % 2 != 0:
            print(k)
            break

