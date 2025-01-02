def solve(s):
    for i in range(2, len(s)):
        if s[i] != s[i-2]:
            return 'NO'
    
    return 'YES'
        

for _ in range(int(input())):
    n = input()
    print(solve(n))