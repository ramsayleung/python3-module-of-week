import re
import string


class MyTemplate(string.Template):
    delimiter = '{{'
    pattern = r'''
        \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
'''
t = MyTemplate('''
{{
{{var}}
''')

print('Matches:', t.pattern.findall(t.template))
print('substituted:', t.safe_substitute(var='replacement'))
