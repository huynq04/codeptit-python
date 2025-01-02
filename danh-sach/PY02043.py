for _ in range(int(input())):
    s, n = input(), input()
    cnt = 0
    l = len(n)
    id = s.find(n)
    while id!= -1:
        cnt+=1
        id = s.find(n, id + l)
    print(cnt)