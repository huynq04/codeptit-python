s1 = set(input().lower().split())
s2 = set(input().lower().split())

hop = s1.union(s2)
sort_list = sorted(hop)

giao = s1.intersection(s2)
sorted_list = sorted(giao)

for i in sort_list:
    print(i, end=' ')
print()
for i in sorted_list:
    print(i, end=' ')
