import string


class Rack:

    def __init__(self, n_max=60):
        self.n_max = n_max
        self.ball_map = [False] * n_max

    def add(self, n):
        self.ball_map[n] = True

    def balls(self):
        return [i for i in range(self.n_max) if self.ball_map[i]]


def char_count(s):
    char_map = {c: 0 for c in string.ascii_lowercase}

    for c in s:
        if c.lower() in string.ascii_lowercase:
            char_map[c.lower()] += 1

    return ''.join([c * n for c, n in char_map.items()])
