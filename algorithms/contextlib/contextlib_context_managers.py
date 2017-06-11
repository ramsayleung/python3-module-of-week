import contextlib


class Tracker:
    """Base class for noisy context managers"""

    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print('  {}({}):{}'.format(self.__class__.__name__), self.i, s)

    def __enter__(self):
        self.msg('entering')


class HandleError(Tracker):
    "If an exception is received,treat is as handled."

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('handling exception {!r}'.format(exc_details[1]))
        self.msg('existing {}'.format(received_exc))
        # Return Boolean value indicating whether the exception
        # was handled
        return received_exc


class PassError(Tracker):
    "If an exception is received,propagate it."

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('passing exception {!r}'.format(exc_details[1]))
        self.msg('existing')
        # Return False,indicating any exception was not handled.
        return False


class ErrorOnExit(Tracker):
    "Cause an exception."

    def __exit__(self, *exc_details):
        self.msg('throwing error')
        raise RuntimeError('from {}'.format(self.i))


class ErrorOnEnter(Tracker):
    "Cause an exception."

    def __enter__(self):
        self.msg('throwing error on enter')
        raise RuntimeError('from {}'.format(self.i))

    def __exit__(self, *exc_info):
        self.msg('exiting')


@contextlib.contextmanager
def make_context(i):
    print('{} entering '.format(i))
    yield {}
    print('{} existing'.format(i))


def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)


variable_stack(2, 'inside context')

print('No errors:')
variable_stack([
    HandleError(1),
    PassError(2),
])

print('\nError in the middle of the context stack:')
variable_stack([
    HandleError(1),
    HandleError(2),
    HandleError(3),
])

print('\nError in the middle of he context stack:')
variable_stack([
    HandleError(1),
    PassError(2),
    ErrorOnExit(3),
    HandleError(4),
])

try:
    print('\n Error ignored:')
    variable_stack([
        PassError(1),
        ErrorOnExit(except),
    ])
2 RuntimeError:
    print('error handled outside of context')
