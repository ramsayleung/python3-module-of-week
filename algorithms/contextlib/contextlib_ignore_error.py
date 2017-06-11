import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        'The operations failed because of existing state'
    )


try:
    print('trying non-idempotent operations')
    non_idempotent_operation()
    print('successded')
except NonFatalError:
    pass

print('done')
