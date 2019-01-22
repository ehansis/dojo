import re


def get_cols():
    with open('weather.dat') as f:
        first_line = f.readline()

    matches = re.finditer(r' +\S+', first_line)

    return {m.group().strip(): {'start': m.start(), 'num': m.end() - m.start()} for m in matches}
