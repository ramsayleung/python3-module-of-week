import enum

BugStatus = enum.Enum(
    value='BugStatus',
    names=('fix_released fix_committed in_pregress wont_fix invalid incomplete new')
)
print('Member:{}'.format(BugStatus.new))
print('\n All members:')
for status in BugStatus:
    print('{:15}={}'.format(status.name, status.value))
