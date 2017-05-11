from urllib.parse import urlsplit

url = 'http://user:pwd@NetLoc:80/p1;para/p2;para?query=arg#frag'
parsed = urlsplit(url)
print(parsed)
print('scheme:', parsed.scheme)
print('netloc:', parsed.netloc)
print('path:', parsed.path)
print('query:', parsed.query)
print('username:', parsed.username)
print('fragment:', parsed.fragment)
print('hostname', parsed.hostname)
print('port:', parsed.port)
