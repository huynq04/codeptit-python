for _ in range(int(input())):
    a = input()
    b = [int(i) for i in a]
    tong = sum(b)
    ok = True
    for i in range(len(a) -1):
        if tong % 10 != 0 or abs(b[i] - b[i+1]) != 2:
            ok = False
    if ok: print("YES")
    else: print("NO")