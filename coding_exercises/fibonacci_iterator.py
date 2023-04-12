class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        c = self.a + self.b
        self.a = self.b
        self.b = c
        return c

if __name__ == '__main__':
    fib = Fibonacci()
    fib_iter = iter(fib)
    print(next(fib_iter))
    print(next(fib_iter))
    print(next(fib_iter))
    print(next(fib_iter))
    print(next(fib_iter))