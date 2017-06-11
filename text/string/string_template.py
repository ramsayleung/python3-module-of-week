import string

values = {'var': 'foo'}
t = string.Template("""
Variable  :$var
Escape :$$
Variable in text :${var}iable
""")

print('Template', t.substitute(values))

s = """
Variable :%(var)s
Escape : %%
Variable in text:%(var)siable
"""

print('interpolation:', s % values)
s = """
Variable :{var}
Escape :{{}}
Variable in text:{var}iable
"""
print('Format:', s.format(**values))
