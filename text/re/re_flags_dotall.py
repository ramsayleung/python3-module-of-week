import re
text = 'This is some text -- with punctuation.\nA second line.'
pattern = r'.+'
dotall = re.compile(pattern, re.DOTALL)
no_newlines = re.compile(pattern)

print('Text:\n {!r}'.format(text))
print('Pattern:\n{}'.format(pattern))
print('No newlines :')
for match in no_newlines.findall(text):
    print(' {!r}'.format(match))

print('DOTALL .....')
for match in dotall.findall(text):
    print(' {!r}'.format(match))
