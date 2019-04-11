def non_whitespace(s):
    # extract all non-whitespace-lines
    lines = [l.strip() for l in s.split('\n')]
    lines = [l for l in lines if len(l) > 0]
    return lines


def non_block_comments(s):
    # extract all lines that are not block comments
    in_block = False
    out = []
    for l in non_whitespace(s):
        if '/*' in l and '*/' not in l and not in_block:
            in_block = True
        elif '*/' in l and in_block:
            in_block = False
        elif not in_block:
            out.append(l)

    return out


def code_lines(s):
    # extract code lines (remove line comments)
    return len([l for l in non_block_comments(s) if not l.startswith('//')])

