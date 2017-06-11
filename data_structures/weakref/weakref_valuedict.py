import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject({})'.format(self.name)

    def __del__(self):
        print('  (deleting{})'.format(self))


def demo(cache_factory):
    # hold objects so any weak references
    # are not removed immediately
    all_refs = {}
    # create the cache using the factory

    print('CACHE TYPE:', cache_factory)
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        obj = ExpensiveObject(name)
        cache[name] = obj
        all_refs[name] = obj
        del obj  # decref

    print(' all_refs =', end=' ')
    pprint(all_refs)
    print('\n Before,cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('   {}={}'.format(name, value))
        del value  # decref

    # remove all references to the objects except the cache
    print('\n Cleanup:')
    del all_refs
    gc.collect()

    print('\n After,cache contains:', list(cache.keys()))

    for name, value in cache.items():
        print('  {}={}'.format(name, value))
    print(' demo returning')

    return
demo(dict)
print()
