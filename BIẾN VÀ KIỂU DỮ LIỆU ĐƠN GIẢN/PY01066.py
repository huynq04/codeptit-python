def solve(s1):
    s2 = s1[::-1]
    for i in range(1, len(s1)):
        if abs(ord(s1[i-1]) - ord(s1[i])) != abs(ord(s2[i-1]) - ord(s2[i])):
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    print(solve(input()))