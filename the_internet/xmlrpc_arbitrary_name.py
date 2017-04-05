from xmlrpc.server import SimpleXMLRPCServer
server = SimpleXMLRPCServer(('localhost', 9000))


def my_funtion(a, b):
    return a * b


server.register_function(my_funtion, 'multiply args')
try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
