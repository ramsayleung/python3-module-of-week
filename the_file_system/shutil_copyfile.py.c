import glob
import shutil

print('Before:', glob.glob('shutil_copyfile.*'))

shutil.copyfile('shutil_copyfile.py', 'shutil_copyfile.py.c')
print('AFTER:', glob.glob('shutil_copyfile.*'))
