import asyncio


async def consumer(condition, n):
    with await condition:
        print('consumer {} is waiting'.format(n))
        await condition.wait()
        print('consumer {} triggred'.format(n))
    print('ending consumer {}'.format(n))


async def manipulate_condition(condition):
    print('starting manipulate_condition')

    await asyncio.sleep(0.1)

    for i in range(1, 3):
        with await condition:
            print('notifying {} consumers'.format(i))
            condition.notify(n=i)
        await asyncio.sleep(0.1)
    with await condition:
        print('notifying remaining consumers')
        condition.notify_all()

    print('ending manipulate_condition')


async def main(loop):
    condition = asyncio.Condition()

    consumers = [
        consumer(condition, i)
        for i in range(5)
    ]

    loop.create_task(manipulate_condition(condition))

    await asyncio.wait(consumers)

event_loop = asyncio.get_event_loop()

try:
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
