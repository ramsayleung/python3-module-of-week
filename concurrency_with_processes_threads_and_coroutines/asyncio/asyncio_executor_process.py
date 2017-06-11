
import asyncio
import concurrent.futures
import logging
import sys
import time


def blocks(n):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n**2


async def run_blocking_tasks(executor):
    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')

    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocksing_tasks = [
        loop.run_in_executor(executor, blocks, i) for i in range(6)
    ]
    log.info('waiting for executor tasks')
    completed, pend = await asyncio.wait(blocksing_tasks)
    results = [t.result() for t in completed]
    log.info('results:{!r}'.format(results))
    log.info('exiting')


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='PID %(process)5s %(name)18s: %(message)s',
        stream=sys.stderr,
    )
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=3)
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()
