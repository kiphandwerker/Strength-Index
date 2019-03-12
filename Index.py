class Person:
    global fullname

    def __init__(self, first, last, BFP):
        self.first = str(first)
        self.last = str(last)
        self.BFP = BFP

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))


class Weightlifter(Person):

    def __init__(self, first, last, weight):
        super().__init__(first, last, weight)
        self.weight = int(weight)

    def totals(self, BP, SQ, DL):
        self.BP = int(BP)
        self.SQ = int(SQ)
        self.DL = int(DL)
        self.total = int(self.BP + self.SQ + self.DL)

    def print_totals(self):
        print(" ")
        print(self.first + " " + self.last)
        print('-->', self.BP, 'Bench Press')
        print('-->', self.SQ, 'Squat')
        print('-->', self.DL, 'Deadlift')
        print('_____________________')
        print('-->', self.total, 'Total', '|', round(self.total / self.weight, 2), 'Strength Index')


w_1 = Weightlifter('Kip','Handwerker',190)

w_1.totals(335,520,550)

Weightlifter.print_totals(w_1)



