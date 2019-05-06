import os
from collections import defaultdict

import numpy as np


def wordlist():
    """Get list of words"""
    filename = os.path.join(os.path.dirname(__file__), '..', 'wordlist.txt')
    with open(filename, encoding='latin1') as f:
        words = f.readlines()

    return [w.strip().lower() for w in words]


def chars_lookup():
    """Build a 2D numpy array of words (rows) and chars (columns)"""
    words = wordlist()
    lmax = max(len(w) for w in words)



def next_words(word, lookup):
    """For an input word, find next words in chain - words with one character changed"""