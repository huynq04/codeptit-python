import re

doc = ''
while True:
    try:
        doc += input()
    except:
        break
lines = re.split('[.?!]', doc)
for line in lines:
    if len(line) == 0:
        continue
    line = line.lower().split()
    line[0] = line[0].title()
    print(' '.join(line))