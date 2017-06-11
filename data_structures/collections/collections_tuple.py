bob = ('Bob', 30, 'male')
print('Representation:', bob)

jane = ('jane', 29, 'female')
print('\nField by index:', jane[0])

print('\n Fields by index:')

for p in [bob, jane]:
    print('{} is a {} year old {}'.format(*p))
