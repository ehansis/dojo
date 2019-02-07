from . import anagrams


class TestAnagrams:

    def test_anagram(self):
        a = anagrams.anagrams()
        assert a[anagrams.keyfunc('enlist')] == ['elints', 'enlist', 'inlets', 'listen', 'silent', 'tinsel']

    def test_all_anagrams(self):
        a = anagrams.anagrams()
        n_a = 0
        for k, v in a.items():
            if len(v) > 1:
                n_a += len(v)

        assert n_a == 48162
        assert sum(len(v) > 1 for v in a.values()) == 20683
