while True:
    x = input()
    if x.split()[0] == '-1': 
        break
    l, r = [int(i) for i in x.split()]
    n = int(input())
    se = set()
    for i in range(l, r+1):
        check = True
        for j in range(2, n+1):
            if i % j == 0:
                check = False
                break
        
        if check:
            se.add(i)

    print(len(se))

