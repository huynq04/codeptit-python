def check(s):
    tong = 0
    tich = 1
    full0 = True
    for i in range(len(s)):
        if i%2==0: 
            tong += int(s[i])
        else:
            if s[i] != '0':
                full0 = False
                tich*=int(s[i])
    
    if full0:
        print(f'{tong} 0')
    else:
        print(f'{tong} {tich}')

for _ in range(int(input())):
   check(input())
        