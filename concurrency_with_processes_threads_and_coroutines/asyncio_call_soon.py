import asyncio
import functools


def callable(arg, *, kwarg='default'):
    print('callable invoked with {} and {}'.format(arg, kwarg))


async def main(loop):
    print('registering callables')
    loop.call_soon(callable, 1)
    wrapped = functools.partial(callable, kwarg='not default')
    loop.call_soon(wrapped, 2)

    await asyncio.sleep(0.1)

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
