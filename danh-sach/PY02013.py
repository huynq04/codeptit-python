while True:
    x = int(input())
    if x == 0: break
    cnt = 1
    while True:
        if x == 1: break
        cnt+=1
        if x % 2 == 0:
            x /= 2
        else:
            x = x * 3 + 1

    print(cnt)