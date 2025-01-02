n, a = int(input()), [float(i) for i in input().split()]

nn = min(a)
ln = max(a)

for i in a:
    if i == nn or i == ln:
        a.remove(i)

avg = sum(a) / len(a)

print(f'{avg:.2f}')
