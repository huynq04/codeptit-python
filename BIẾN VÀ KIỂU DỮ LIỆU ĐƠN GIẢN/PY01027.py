def check(s):
    for i in s:
        if i != '6' and i != '8':
            return 'NO'
        if s.find('888') != -1:
            return 'NO'
        
    return 'YES'

print(check(input()))