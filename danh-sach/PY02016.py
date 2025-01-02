from collections import Counter

def solve(a):
    cnt_a = Counter(a).items()
    maxx = 0 
    key = 0
    for k, v in cnt_a:
        if v > maxx:
            maxx = v
            key = k
    if maxx > len(a) / 2:
        return key
    else:
        return 'NO'
    
    
        

for _ in range(int(input())):
    n = input()
    a = [int(i) for i in input().split()]
    print(solve(sorted(a)))