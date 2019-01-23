import hashlib
import numpy as np

n = 7
table_size = 2_000_000


def hashes(s):
    s = s.encode('utf8')
    return sorted(int(hashlib.sha256(s + bytes(i)).hexdigest(), base=16) % table_size
                  for i in range(n))


def set_bits(h, a=None):
    if a is None:
        a = np.zeros(table_size, dtype=bool)
    a[h] = True
    return a


def store_word(s, a=None):
    return set_bits(hashes(s), a=a)


def find_word(s, a):
    return a[hashes(s)].all()
