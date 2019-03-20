# noinspection PyUnresolvedReferences
from typing import List, Tuple

from os import path


def wordlist():
    with open(path.join(path.dirname(__file__), '..', 'wordlist.txt'), encoding='latin1') as f:
        words = [w.strip() for w in f.readlines()]
    return words


def readable(words):
    """Readable version (170 ms per call)

    Goal: find six-letter words in wordlist that are composed of two other words that are also in the word list.

    Returns:
        List[Tuple(str, str, str)]: first element is composed word, concatenating the other two values of
            the tuple gives the composed word
    """

    # extract all six-letter words
    sixletter = [w for w in words if len(w) == 6]

    # build a lookup table from word length (key) to words of that length, for all candidate
    # constituent words (these have to have 5 letters or less)
    candidates = dict()
    for w in words:
        n = len(w)
        if n <= 5:
            if n not in candidates:
                candidates[n] = set()
            candidates[n].add(w)

    # Find results: Iterate over six-letter words, for each check if any sub-word is in the word list
    # and if so, check if the rest of the word also is in the word list.
    results = list()
    for s in sixletter:
        # check from 1 up to 5 characters for first word part
        for i in range(1, 6):
            front = s[:i]
            back = s[i:]
            if front in candidates[i] and back in candidates[6 - i]:
                # we found a pair, add it to the results
                results.append((s, front, back))

    return results


def fast(words):
    """Fast version (146 ms per call)"""

    # build a lookup table from word length (key) to words of that length
    candidates = dict()
    for w in words:
        n = len(w)
        if n <= 6:
            candidates.setdefault(n, set()).add(w)

    # Find results: Iterate over six-letter words, for each check if any sub-word is in the word list
    # and if so, check if the rest of the word also is in the word list.
    results = list()
    for s in candidates[6]:
        # check from 1 up to 5 characters for first word part
        for i in range(1, 6):
            if s[:i] in candidates[i]:
                if s[i:] in candidates[6 - i]:
                    # we found a pair, add it to the results
                    results.append((s, s[:i], s[i:]))

    return results


def extensible(words, word_len):
    """Extensible version"""

    nletter = [w for w in words if len(w) == word_len]

    candidates = dict()
    for w in words:
        n = len(w)
        if n < word_len:
            if n not in candidates:
                candidates[n] = set()
            candidates[n].add(w)

    results = list()
    for s in nletter:
        for i in range(1, word_len):
            front = s[:i]
            back = s[i:]
            if front in candidates[i] and back in candidates[word_len - i]:
                results.append((s, front, back))

    return results
