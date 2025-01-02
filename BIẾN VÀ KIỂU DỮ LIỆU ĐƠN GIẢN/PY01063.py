for _ in range(int(input())):
    s = input()
    n = input()

    cnt = 0
    id = s.find(n)
    while id != -1:
        cnt +=1
        id = s.find(n, id+len(n))
    print(cnt)
