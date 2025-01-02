from datetime import datetime


class TS:
    def __init__(self, ten, tinh, gio):
        self.ten = ten
        self.tinh = tinh
        id = ''
        gio = (datetime.strptime(gio, '%H:%M') - datetime.strptime('06:00', '%H:%M')).seconds / 3600
        self.vt = 120 / gio
        for i in tinh.split():
            id += i[0].upper()
        for i in ten.split():
            id += i[0].upper()
        self.id = id
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.tinh} {round(self.vt)} Km/h'

a =[]    
for i in range(int(input())):
    a.append(TS(input(), input(), input()))

a.sort(key=lambda e: -e.vt)
print(*a, sep='\n')

        