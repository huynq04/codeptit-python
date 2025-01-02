while True:
    n = int(input())
    if n ==0: break
    a = []
    for i in range(n):
        a.append(int(input()))
    if len(set(a)) > 1:
        print(min(a), end=' ')
        print(max(a))
    else:
        print('BANG NHAU')
