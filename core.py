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


def solve(fn, day, *args, **kwargs):
    return fn(read_input(day), *args, **kwargs)


def solve_sample(fn, sample, *args, **kwargs):
    return fn(read_sample_input(sample), *args, **kwargs)


def xor(a, b):
    return bool(a) ^ bool(b)
