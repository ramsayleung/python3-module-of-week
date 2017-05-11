import logging
import logging.handlers

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)
socketHandler = logging.handlers.SocketHandler('localhost',
                                               port=10000)
# don't bother with a formatter, since a socket handler sends the event as
# an unformatted pickle
rootLogger.addHandler(socketHandler)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info(b'Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug(b'Quick zephyrs blow, vexing daft Jim.')
logger1.info(b'How quickly daft jumping zebras vex.')
logger2.warning(b'Jail zesty vixen who grabbed pay from quack.')
logger2.error(b'The five boxing wizards jump quickly.')
