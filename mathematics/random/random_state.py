import os
import pickle
import random

if os.path.exists('state.dat'):
    # Restore the previously saved state
    print('Found state.dat, initializing random module')
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Use a well-known start state
    print('No state.dat, seeding')
    random.seed(1)

# Produce random values
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

# Save state for next time
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

# Produce more random value
print('\nAfter saving state:')
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()
