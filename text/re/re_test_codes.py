from re_test_patterns import test_patterns

test_patterns(
    'A prime #1 example',
    [(r'\d+', 'sequences of digits'),
     (r'\D+', 'sequences of non-digits'),
     (r'\s+', 'sequences of whitespace'),
     (r'\S+', 'sequences of non-whitespace'),
     (r'\w+', 'alphanumberic character '),
     (r'\W+', 'non-alphanumberic')
     ],
)
