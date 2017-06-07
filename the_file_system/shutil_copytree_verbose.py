import glob
import pprint
import shutil


def verbose_copy(src, dst):
    print('copying \n{!r}\n to {!r}'.format(src, dst))
    return shutil.copy2(src, dst)


print('BEFORE:')
pprint.pprint(glob.glob('/tmp/example/*'))
print()


shutil.copytree(
    '.', '/tmp/example',
    copy_function=verbose_copy,
    ignore=shutil.ignore_patterns('*.py'),
)
print('\nAFTER:')
pprint.pprint(glob.glob('/tmp/example/*'))
