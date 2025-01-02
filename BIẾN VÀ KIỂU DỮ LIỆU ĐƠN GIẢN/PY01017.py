for _ in range(int(input())):
    s = input()
    cnt = 1
    l = len(s)
    for i in range(1, l):
        if s[i] != s[i-1]:
            print(cnt, end='')
            print(s[i-1], end='')
            cnt = 1
        else:
            cnt += 1

    print(cnt, end = '')
    print(s[l - 1])
