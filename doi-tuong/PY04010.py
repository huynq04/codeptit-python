class ThiSinh:
    def __init__(self, ten, ns, diem):
        self.ten = ten
        self.ns = ns
        self.tong = sum(diem)

    def __str__(self):
        return f'{self.ten} {self.ns} {self.tong}'
    

name = input()
dob = input()
marks = [float(input()), float(input()), float(input())]
print(ThiSinh(name, dob, marks))
        