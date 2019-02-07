import os
import itertools


def keyfunc(w):
    return ''.join(sorted(w))


def anagrams():
    fname = os.path.join(os.path.dirname(__file__), '..', 'wordlist.txt')
    with open(fname, encoding='latin1') as f:
        lines = f.readlines()

    return {k: list(g) for k, g in itertools.groupby(
        (l.strip() for l in sorted(lines, key=keyfunc)), key=keyfunc)}
