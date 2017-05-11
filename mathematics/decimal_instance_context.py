import decimal

c = decimal.getcontext().copy()
c.prec = 3

pi = c.create - decimal('3.1415')

print('PI:', pi)

print('RESTULT:', decimal.Decimal('2.01') * pi)
