from kata20190123 import bloom


class TestBloom:

    def test_hashes(self):
        h = bloom.hashes('abc')
        assert len(h) == 5
        assert len(set(h)) == len(h)
        assert all(0 < i < 32768 for i in h)

        k = bloom.hashes('abc')
        assert h == k

        l = bloom.hashes('abcd')
        assert l != k

    def test_set_bits(self):
        a = bloom.set_bits([0, 1, 3])
        assert a[0]
        assert a[1]
        assert not a[2]
        assert a[3]
        assert not a[4]

        bloom.set_bits([2], a=a)
        assert a[0]
        assert a[1]
        assert a[2]
        assert a[3]
        assert not a[4]

    def test_store_word(self):
        a = bloom.store_word('abc')
        assert a.sum() == 5

    def test_find_word(self):
        a = None
        a = bloom.store_word('abc', a)
        assert bloom.find_word('abc', a)
        assert not bloom.find_word('abcd', a)
        a = bloom.store_word('abcd', a)
        assert bloom.find_word('abcd', a)

    def test_collisions(self):
        with open('/usr/share/dict/words') as f:
            words = [w.strip() for w in f.readlines()]

        print(len(words))

        collisions = 0
        a = None
        for w in words:
            if a is not None:
                collisions += bloom.find_word(w, a)
            a = bloom.store_word(w, a)

        print(collisions, collisions / len(words))
