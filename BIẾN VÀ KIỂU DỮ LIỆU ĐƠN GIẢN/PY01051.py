def solve(n):
    cnt = 0
    for i in n:
        cnt += int(i)

    cnt = str(cnt)
    if len(cnt) == 1:
        return 'NO'
    if cnt != cnt[::-1]: 
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    print(solve(input()))