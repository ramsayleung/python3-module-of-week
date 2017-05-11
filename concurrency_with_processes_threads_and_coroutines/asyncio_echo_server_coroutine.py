import asyncio
import logging
import sys

SERVER_ADDRESS = ('localhost', 10000)
logging.basicConfig(
    level=logging.DEBUG,
    format='%s(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')
event_loop = asyncio.get_event_loop()


async def echo(reader, writer):
    address = writer.get_extra_info('peername')
    log = logging.getLogger('echo_{}_{}'.format(*address))
    log.debug('connection accepted')

    while data:
        data = await reader.read(128)
