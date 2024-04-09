#homework 7
#1
from decimal import Decimal

class frange:
    def __init__(self, start, stop, step):
        self.start = Decimal(str(start))
        self.stop = Decimal(str(stop))
        self.step = Decimal(str(step))
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            current = self.current
            self.current += self.step
            return float(current)
        else:
            raise StopIteration

for i in frange(1, 100, 3.5):
    print(i)
#2
class Colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            print('\033[91m', end='')
        elif self.color == 'green':
            print('\033[92m', end='')
        elif self.color == 'yellow':
            print('\033[93m', end='')
        elif self.color == 'blue':
            print('\033[94m', end='')
        elif self.color == 'magenta':
            print('\033[95m', end='')
        elif self.color == 'cyan':
            print('\033[96m', end='')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('\033[0m', end='')

print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')

with Colorizer('red'):
    print('printed in red')
print('printed in default color')