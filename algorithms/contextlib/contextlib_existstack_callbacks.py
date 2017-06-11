import contextlib


def callback(*args, **kwds):
    print('closing callback({},{})'.format(args, kwds))


with contextlib.ExitStack() as stack:
    stack.callback(callback, 'args1', 'arg2')
    stack.callback(callback, arg3='val3')
