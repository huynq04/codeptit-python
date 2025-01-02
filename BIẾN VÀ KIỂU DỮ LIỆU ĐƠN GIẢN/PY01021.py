for _ in range(int(input())):
    s = input()
    a = []
    tong = 0
    for c in s:
        if c.isalpha():
            a.append(c)
        elif c.isdigit():
            tong += int(c)
    a.sort()
    for c in a:
        print(c, end='')
    print(tong)