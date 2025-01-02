def solve(s):
    for i in s:
        if i!= '0' and i!='2' and i != '1':
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    s = input()
    print(solve(s))
    
            