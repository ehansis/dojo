from . import objectives


class TestWordlist:

    def test_wordlist(self):
        w = objectives.wordlist()
        assert len(w) == 338_882


class TestReadable:

    def test_tdd(self):
        words = objectives.wordlist()
        results = objectives.readable(words)
        assert len(results) > 100
        print(len(results))

        for r in results:
            assert r[0] == r[1] + r[2]

        assert ('albums', 'al', 'bums') in results
        assert ('weaver', 'we', 'aver') in results

    def test_profiling(self):
        words = objectives.wordlist()
        for _ in range(100):
            objectives.readable(words)


class TestFast:

    def test_tdd(self):
        words = objectives.wordlist()
        results = objectives.fast(words)
        assert len(results) > 100
        print(len(results))

        for r in results:
            assert r[0] == r[1] + r[2]

        assert ('albums', 'al', 'bums') in results
        assert ('weaver', 'we', 'aver') in results

    def test_profiling(self):
        words = objectives.wordlist()
        for _ in range(100):
            objectives.fast(words)


class TestExtensible:

    def test_tdd(self):
        for i in [4, 6, 8]:
            words = objectives.wordlist()
            results = objectives.extensible(words, i)
            assert len(results) > 100
            print(len(results))
            print(results[1000])
            print(results[5000])

            for r in results:
                assert len(r[0]) == i
                assert r[0] == r[1] + r[2]
