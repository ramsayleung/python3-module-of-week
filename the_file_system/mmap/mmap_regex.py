import mmap
import re

pattern = re.compile(
    rb'(\.\w+)?([^.]?nulla[^.]*?\.)', re.DOTALL | re.IGNORECASE | re.MULTILI)

with open('lorem.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        for match in pattern.findall(m):
            print(match[1].replace(b'\n', b' '))
