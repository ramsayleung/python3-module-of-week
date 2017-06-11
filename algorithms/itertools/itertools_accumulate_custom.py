from itertools import *


def f(a, b):
    print(a, b)
    return b + a + b


print(list(accumulate('abcde', f)))
