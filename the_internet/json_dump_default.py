import json

import json_myobj

obj = json_myobj.Myobj('instance value goes here')

print('First attempt')
try:
    print(json.dumps(obj))
except TypeError as err:
    print('Error:', err)


def convert_to_builtin_type(obj):
    print('default(', repr(obj), ')')
    d = {
        '__class__': obj.__class__.__name__,
        '__module__': obj.__module__,
    }
    d.update(obj.__dict__)
    return d


print()
print('with default')
print(json.dumps(obj, default=convert_to_builtin_type))
