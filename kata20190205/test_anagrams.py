from . import anagrams


class TestAnagrams:

    def test_words(self):
        words = anagrams.words()
        assert len(words) == 338882
        assert sum(len(w) == 0 for w in words) == 0

    def test_lookup_table(self):
        words = ['abc', 'ab', 'cba', 'aa', 'acb', 'ba']
        t = anagrams.lookup_table(words)
        assert t == {
            'abc': ['abc', 'cba', 'acb'],
            'ab': ['ab', 'ba'],
            'aa': ['aa']
        }

    def test_anagram(self):
        t = anagrams.lookup_table(anagrams.words())
        assert anagrams.anagram('enlist', t) == ['elints', 'enlist', 'inlets', 'listen', 'silent', 'tinsel']
        assert anagrams.anagram('foooooo', t) == []

    def test_all_anagrams(self):
        n_a = 0
        words = anagrams.words()
        table = anagrams.lookup_table(words)
        for w in words:
            a = anagrams.anagram(w, table)
            if len(a) > 1:
                n_a += 1

        assert n_a == 48162
        assert sum(len(v) > 1 for v in table.values()) == 20683
