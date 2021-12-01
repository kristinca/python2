class Fibo:

    def __init__(self, *args, **kwargs):
        self.fib1 = 0
        self.fib2 = 1
        self.fib_end = 7

    def __iter__(self):
        return self

    def next_elem(self):
        val = self.fib1
        self.fib1 = self.fib2
        self.fib2 = val+self.fib2

        return val

    def iterator(self, to_do):
        """Iterator for the numbers from start"""
        i = 0
        while i < self.fib_end:
            i += 1
            try:
                next_el = self.next_elem()
            except StopIteration:
                break
            else:
                to_do(next_el)


def main():
    fibo = Fibo()
    fibo.iterator(print)


if __name__ == '__main__':
    main()
