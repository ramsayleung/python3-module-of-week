import asyncio
import time


def callable(n, loop):
    print('callable {} invoked at {}'.format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print('clock time:{}'.format(time.time()))
    print('loop time:{}'.format(now))

    print('registering callables')

    loop.call_at(now + 0.2, callable, 1, loop)
    loop.call_at(now + 0.1, callable, 2, loop)
    loop.call_soon(callable, 3, loop)

    await asyncio.sleep(1)

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
