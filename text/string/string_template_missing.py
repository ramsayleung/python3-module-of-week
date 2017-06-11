import string

values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute():', t.substitute(values))
except KeyError as err:
    print('Error:', str(err))
print('safe_substitue():', t.safe_substitute(values))
