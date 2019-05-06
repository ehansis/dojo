from . import wordchain


def test_wordlist():
    w = wordchain.wordlist()
    assert len(w) == 338882
    assert all(len(ww) > 0 for ww in w)


def test_chars_lookup():
    c = wordchain.chars_lookup()
    assert len(c['loo']) == 3
    assert 'look' in c['loop']
    assert 'loop' in c['loop']


def test_next_words():
    l = wordchain.chars_lookup()
    w = wordchain.next_words('pool', l)
    assert len(w) > 2
    assert 'poor' in w
