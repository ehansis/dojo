import io

from . import trigrams

test_text = "This is test text. With\n\nnewlines, and punctuation!"


def test_load_words():
    f = io.StringIO(test_text)
    w = trigrams.load_words(f)
    assert w == ['This', 'is', 'test', 'text.', 'With', 'newlines,', 'and', 'punctuation!']


def test_trigrams():
    f = io.StringIO(test_text + " " + test_text)
    w = trigrams.load_words(f)
    t = trigrams.trigrams(w)

    assert len(t) == 6 + 2
    assert t[('This', 'is')] == ['test', 'test']
    assert t[('is', 'test')] == ['text.', 'text.']
    assert t[('and', 'punctuation!')] == ['This']


