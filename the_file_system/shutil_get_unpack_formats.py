import shutil

for format, exts, description in shutil.get_unpack_formats():
    print('{:<5}: {},name ending in {}'.format(format, description, exts))
