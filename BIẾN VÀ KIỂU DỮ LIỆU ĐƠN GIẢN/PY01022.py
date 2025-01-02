a = input()
cnt = 0
while len(a) > 1:
    tong = 0
    cnt += 1
    for i in a:
        tong += ord(i) - ord('0')
    a = str(tong)

print(cnt if cnt > 0 else 1)


