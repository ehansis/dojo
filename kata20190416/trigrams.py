from collections import defaultdict
import random


def load_words(f):
    text = f.read()
    words = text.split()
    return words


def trigrams(words):
    t = defaultdict(list)
    for i in range(len(words) - 2):
        t[(words[i], words[i + 1])].append(words[i + 2])
    return t


def make_text(trig, min_words):
    text = ""
    sentence_end = ".!?"

    def _rand_start():
        # start at a new sentence start
        return random.choice([k for k in trig.keys() if k[1][-1] in sentence_end])

    done = False
    n = 0
    current = _rand_start()

    while not done:
        word = random.choice(trig[current])
        text += " " + word
        n += 1

        current = (current[1], word)
        if current not in trig:
            current = _rand_start()

        if n >= min_words and word[-1] in sentence_end:
            done = True

    return text


if __name__ == "__main__":
    with open('../tom_swift_airship.txt') as f:
        words = load_words(f)
        t = trigrams(words)
        print(make_text(t, 300))