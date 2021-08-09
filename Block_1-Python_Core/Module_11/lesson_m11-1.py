class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file_handler = None

    def __enter__(self):
        self.file_handler = open(self.filename, self.mode)
        return self.file_handler

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_handler.close()


if __name__ == "__main__":
    with OpenFile("____________", "r") as f:
        print(f.read())
#
###################################
#
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class FibIterator:
    def __init__(self, count):
        self.count = count
        self.generated_numbers = 0

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.generated_numbers = 0
        return self

    def __next__(self):
        if self.generated_numbers <= self.count:
            self.a, self.b = self.b, self.a + self.b
            self.generated_numbers += 1
            return self.a
        else:
            raise StopIteration


if __name__ == "__main__":
    for value in FibIterator(10):
        print(value)
#
#################################
#
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class FibIterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.generated_numbers = 0
        return self

    def __next__(self):
        if self.generated_numbers > self.count:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.generated_numbers += 1
        return self.a


if __name__ == "__main__":
    for value in FibIterator(10):
        print(value)
#
###################################
