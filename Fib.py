import sys


class Fib:
    '''iterator that yields numbers in Fibonacci sequence'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == '__main__':
    b = Fib(1000)
    print(b)
    print(b.__class__)
    print(b.__doc__)
    for a in b:
        sys.stdout.write(str(a) + ' ')
