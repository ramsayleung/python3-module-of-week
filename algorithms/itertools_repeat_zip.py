from itertools import repeat, count
for i, s in zip(count(), repeat('over-and-over', 5)):
    print(i, s)
