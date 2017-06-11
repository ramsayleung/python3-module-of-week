import contextlib


@contextlib.contextmanager
def make_context():
    print('  entering')
    try:
        # Yield control,but not a value,because any value
        # Yielded is not available when context manager
        # is used as decorator
        yield
    except RuntimeError as err:
        print('  Error:', err)
    finally:
        print('  existing')


@make_context()
def normal():
    print('  inside with statement')


@make_context()
def throw_error(error):
    raise error


print('Normal')
normal()

print('\nHandled error:')
throw_error(RuntimeError('showing example of handling an error'))

print('\nUnhandled error:')
throw_error(ValueError('this exception is  not handled'))
