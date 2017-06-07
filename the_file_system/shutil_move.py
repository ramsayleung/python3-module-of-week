import glob
import shutil

with open('example.txt', 'wt') as f:
    f.write('content')

print('BEFORE:', glob.glob('example*'))

shutil.move('example.txt', 'example.out')
print('AFTER:', glob.glob('example*'))
