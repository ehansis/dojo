from collections import defaultdict
import random
import re
import fysom


def load_words(file):
    text = file.read()

    # replace single newlines (and other white space) with single space, double newlines with space+newline;
    # when splitting on spaces later, this keeps paragraph ends.
    text = text.replace('\n\n', '_PAR_')
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('_PAR_', '\n ')

    words = text.split(' ')
    return [w for w in words if len(w) > 0]


def trigrams(words):
    t = defaultdict(list)
    for i in range(len(words) - 2):
        t[(words[i], words[i + 1])].append(words[i + 2])
    return t


def make_text(trig, min_words):
    text = ""
    sentence_end = ".!?"
    quotmark = '"'

    fsm = fysom.Fysom(
        {'initial': 'text',
         'events': [
             {'name': 'quotstart', 'src': 'text', 'dst': 'quotation'},
             {'name': 'quotend', 'src': 'quotation', 'dst': 'text'},
             {'name': 'enough', 'src': 'text', 'dst': 'longenough'}
         ]
         })

    new_sentence = [k for k in trig.keys() if k[1][-1] in sentence_end]

    done = False
    n = 0
    current = random.choice(new_sentence)

    while not done:
        word = None
        quot_end = [w for w in trig[current] if w.endswith(quotmark)]
        sent_end = [w for w in trig[current] if w.endswith(sentence_end)]
        no_quot_end = [w for w in trig[current] if not w.endswith(quotmark)]
        no_quot_start = [w for w in trig[current] if not w[0] == quotmark]

        if fsm.isstate('quotation'):
            # chose a quotation end, if possible, don't choose a new quotation start
            if len(quot_end) > 0:
                word = random.choice(quot_end)
            elif len(no_quot_start) > 0:
                word = random.choice(no_quot_start)
        elif fsm.isstate('longenough'):
            # don't start a new quotation if the text is long enough (if possible), try to choose sentence end
            if len(sent_end) > 0:
                word = random.choice(sent_end)
            elif len(no_quot_start) > 0:
                word = random.choice(no_quot_start)

        # default choice, try not to choose a quotation end
        if word is None:
            if len(no_quot_end) > 0:
                word = random.choice(no_quot_end)
            else:
                word = random.choice(trig[current])

        text += " " + word
        n += 1

        if word[0] == quotmark and fsm.isstate('text'):
            fsm.quotstart()
        if word[-1] == quotmark and fsm.isstate('quotation'):
            fsm.quotend()

        current = (current[1], word)
        if current not in trig:
            current = random.choice(new_sentence)

        if n >= min_words:
            if fsm.isstate('text'):
                fsm.enough()

        if fsm.isstate('longenough') and word[-1] in sentence_end:
            done = True

    return text


if __name__ == "__main__":
    with open('../tom_swift_airship.txt') as f:
        ws = load_words(f)
        txt = trigrams(ws)
        print(make_text(txt, 100))
