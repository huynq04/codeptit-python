def check(s: str):
    a = s.split('.')

    for i in a:
        if i.isdigit():
            i = int(i)
        else:
            a.remove(i)

    if len(a) != 4 :
        return 'NO'

    for i in a:
        if int(i) < 0 or int(i) > 255:
            return 'NO'

    return 'YES' 
    

for _ in range(int(input())):
    print(check(input()))
    