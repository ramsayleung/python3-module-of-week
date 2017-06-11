import asyncio


def callable(n):
    print('callable {} invoked'.format(n))


async def main(loop):
    print('registering callables')
    loop.call_later(0.2, callable, 1)
    loop.call_later(0.2, callable, 1)
    loop.call_soon(callable, 3)

    await asyncio.sleep(0.4)

event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
