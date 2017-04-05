import xmlrpc.client
import xml.parsers.expat

server = xmlrpc.client.ServerProxy('http://localhost:9000')

s = b'This is a string with control character\x00'
print('Local string:', s)

data = xmlrpc.client.Binary(s)
response = server.send_back_binary(data)
print('as binary:', response.data)

try:
    print('as string:', server.show_type(s))
except xml.parsers.expat.ExpatError as err:
    print('\nError:', err)
