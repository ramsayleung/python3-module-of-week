import collections
a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
m = collections.ChainMap(a, b)
print(m.maps)
print('c={}'.format(m['c']))

# reverse the list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c={}'.format(m['c']))
