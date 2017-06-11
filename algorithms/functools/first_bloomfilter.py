from hashlib import sha256


class BloomFilter(object):
    """A simple bloom filter for lots of int()
    """

    def __init__(self, array_size=(1 * 1024), hashes=13):
        """Initializes a BloomFilter() object
        Expects:
        array_size (int bytes):4*1024 for a 4kb filter
        hashes(int):for the number of hashes to perform
        """
        self.filter = bytearray(array_size)  # The filter itself
        self.bitcount = array_size * 8  # Bits in the filter
        self.hashes = hashes  # The number of hashes to use

    def _hash(self, value):
        """Create a hash of an int and yields a generator of hash function
        Expects:
            value: int()
        Yields:
            generator of ints()
        """
