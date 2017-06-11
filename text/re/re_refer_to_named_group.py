import re
address = re.compile(
    '''
    # The regular name
    (?P<first_name>\w+)
    \s+
    (([\w.]+)\s+)? # optional middle name or initials
    (?P<last_name>\w+)
    
    \s+
    
    <
    # The address: first_name.last_name@domain.tld
    (?P<email>
    (?P=first_name)
    \.
    (?P=last_name)
    @
    ([\w\d.]+\.)+ # domain name prefix
    (com|org|edu)
)
    >
    ''',
    re.VERBOSE | re.IGNORECASE
)
candidates = [
    u'First Last <first.last@example.com>',
    u'Different Name <first.last@example.com>',
    u'First Middle Last <first.last@example.com>',
    u'First M. Last <first.last@example.com>',
]
for candidate in candidates:
    print('Candidate:', candidate)
    match = address.search(candidate)
    if match:
        print(' Match name :', match.groupdict()['first_name'], end=' ')
        print(match.groupdict()['last_name'])
        print('  Match email:', match.groupdict()['email'])
    else:
        print('  No match')
