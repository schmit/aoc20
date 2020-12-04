import operator
import toolz.curried as tz


def read_input(day, path="input/"):
    with open(f"{path}{day}", "r") as f:
        for line in f:
            yield line.strip()


def read_sample_input(s):
    for line in s.split("\n"):
        yield line.strip()


def prod(seq):
    return tz.reduce(operator.mul, seq, 1)


def solve(fn, day):
    return fn(read_input(day))


def solve_sample(fn, sample):
    return fn(read_sample_input(sample))


def xor(a, b):
    return bool(a) ^ bool(b)
