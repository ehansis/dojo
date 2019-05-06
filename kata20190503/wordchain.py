import os

import numpy as np
import networkx as nx


class CacheDict:
    def __init__(self, get_func):
        self.d = dict()
        self.get_func = get_func

    def __getitem__(self, key):
        if key not in self.d:
            self.d[key] = self.get_func(key)
        return self.d[key]


def wordlist():
    """Get list of words"""
    filename = os.path.join(os.path.dirname(__file__), '..', 'wordlist.txt')
    with open(filename, encoding='latin1') as f:
        words = f.readlines()

    return [w.strip().lower() for w in words]


def chars_lookup(word_len, words):
    """Build a 2D numpy array of words (rows) and chars (columns)"""
    n_words = [w for w in words if len(w) == word_len]
    lookup = [list(w) for w in n_words]
    return np.array(lookup), np.array(n_words)


class WordChain:

    def __init__(self, n):
        self.wordlist = wordlist()
        self.n = n
        self.lookup, self.n_words = chars_lookup(self.n, self.wordlist)

    def next_words(self, word):
        """For an input word, find possible next words in chain - words with one character changed"""
        char_masks = np.hstack(self.lookup[:, [i]] == c for i, c in enumerate(word))
        candidates = set()
        for i in range(self.n):
            is_possible = char_masks[:, :i].all(axis=1) & char_masks[:, i+1:].all(axis=1)
            candidates |= set(self.n_words[is_possible])

        return candidates

    def chain(self, start, end):
        g = nx.DiGraph()
        seen = {start}
        candidates = {start}

        g.add_node(start)

        while end not in seen and len(candidates) > 0:
            new_candidates = set()
            for c in candidates:
                nw = self.next_words(c)
                new_candidates |= nw
                g.add_edges_from([(c, w) for w in nw])

            candidates = new_candidates - seen
            seen |= candidates

        return nx.shortest_path(g, source=start, target=end)


