import os
from collections import defaultdict


def words():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'wordlist.txt')
    with open(file_path, encoding='latin1') as f:
        lines = f.readlines()

    return [w.strip() for w in lines]


def lookup_table(word_list):
    t = defaultdict(list)
    for w in word_list:
        t[''.join(sorted(w))].append(w)
    return t

def anagram(word, lookup):
    s = ''.join(sorted(word))
    return sorted(lookup.get(s, []))

