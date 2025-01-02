def solve(s):
    if len(s) < 3:
        return 'NO'
    a = [int(i) for i in s]
    tang = True
    for i in range(1, len(s)):
        if tang and a[i] <= a[i-1]:
            tang = False
        elif not tang and a[i] >= a[i-1]:
            return 'NO'
    return 'YES'

for _ in range(int(input())):
    print(solve(input())) 