from . import wordchain


def test_wordlist():
    w = wordchain.wordlist()
    assert len(w) == 338882
    assert all(len(ww) > 0 for ww in w)


def test_candidates():
    w = wordchain.WordChain(4)
    n = w.next_words('pool')
    assert len(n) > 2
    assert 'pool' in n
    assert 'tool' in n
    assert 'poll' in n
    assert 'poor' in n


def test_wordchain():
    w = wordchain.WordChain(3)
    c = w.chain('cat', 'dog')
    print(c)
    assert len(c) == 4

    w = wordchain.WordChain(4)
    c = w.chain('lead', 'gold')
    print(c)

    # w = wordchain.WordChain(6)
    # c = w.chain('apple', 'grape')
    # print(c)
