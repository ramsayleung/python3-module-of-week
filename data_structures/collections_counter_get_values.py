import collections
c = collections.Counter('abcdaab')
for letter in 'abcde':
    print('{} :{}'.format(letter, c[letter]))
