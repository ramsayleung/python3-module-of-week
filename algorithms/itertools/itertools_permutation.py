from itertools import *


def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()


print('All permutations:\n')

show(premutations('abcd'))

print('\nPairs:\n')
show(premutations('abcd', r=2))
