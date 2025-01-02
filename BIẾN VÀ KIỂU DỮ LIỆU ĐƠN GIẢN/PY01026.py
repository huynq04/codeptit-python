from collections import Counter


for t in range(int(input())):
    s1, s2 = list(input()), list(input())
    print(f'Test {t+1}: ', end='')
    if (Counter(s1)==Counter(s2)):
        print('YES')
    else:
        print('NO')
