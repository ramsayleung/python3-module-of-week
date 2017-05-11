import asyncio


async def consumer(n, q):
    print('consumer {}: starting'.format(n))
    while True:
        print('consumer {}: waiting for item'.format(n))
        item = await q.get()
        print('consumer {}: has item {}'.format(n, item))
        if item is None:
            # None is the signal to stop
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
    print('consumer {}: ending'.format(n))


async def producer(q, num_workers):
    print('producer:starting')
    for i in range(num_workers * 3):
        await q.put(i)
        print('producer: added task {} to the queue'.format(i))

    print('producer:ading stop signal to the queue')
    for i in range(num_workers):
        await q.put(None)
    print('producer:waiting for queue to empty')
    await q.join()
    print('producer:ending')


async def main(loop, num_consumers):
    q = asyncio.Queue(maxsize=num_consumers)

    consumers = [
        loop.create_task(consumer(i, q))
        for i in range(num_consumers)
    ]

    prod = loop.create_task(producer(q, num_consumers))

    await asyncio.wait(consumers + [prod])

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, 2))
finally:
    event_loop.close()
