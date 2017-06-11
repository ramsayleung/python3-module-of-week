import decimal

context = decimal.getcontext()

print('Emax    =', context.Emax)
print('Emin    =', context.Emin)
print('capitals=', context.capitals)
print('prec    =', context.prec)
print('rounding=', context.rounding)
print('flags   =')
for f, v in context.flags.items():
    print('   {}:{}'.format(f, v))
print('trags   =')
for f, v in context.traps.items():
    print('   {}:{}'.format(f, v))
