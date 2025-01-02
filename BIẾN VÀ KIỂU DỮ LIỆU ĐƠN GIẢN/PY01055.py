def check(s):
    if len(s) % 2 == 0:
        return 'NO'
    if s[0] == s[1]:
        return 'NO'
    for i in range(2, len(s), 2):
        if s[i] != s[i-2]:
            return 'NO'
    return 'YES'

for _  in range(int(input())):
    print(check(input()))