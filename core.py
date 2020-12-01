import operator
import toolz.curried as tz


def read_input(day, path="input/"):
    with open(f"{path}{day}", "r") as f:
        for line in f:
            yield line


def read_sample_input(s):
    for line in s.split("\n"):
        if len(line) > 0:
            yield line


def prod(seq):
    return tz.reduce(operator.mul, seq, 1)


def solve(fn, day):
    return fn(read_input(day))


def solve_sample(fn, sample):
    return fn(read_sample_input(sample))
