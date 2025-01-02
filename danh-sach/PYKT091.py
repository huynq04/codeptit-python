from collections import Counter


f = open('VANBAN.in', 'r')

a = []

for line in f:
    a += line.split()

b = Counter(a).items()

maxx = 0
key = ''

se = {}
for k, v in b:
    if k == k[::-1] and len(k) > len(key):
        maxx = v
        key = k

for k, v in b:
    if k == k[::-1] and len(k) == len(key):
        se[k] = v

for k, v in se.items():
    print(f'{k} {v}')