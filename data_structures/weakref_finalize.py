import weakref


class ExpensiveObject():

    def __del__(self):
        print('(deleting {})'.format(self))


def on_finalize(*args):
    print('on_finalize({!r})'.format(args))

obj = ExpensiveObject()
weakref.finalize(obj, on_finalize, 'extra argument')
