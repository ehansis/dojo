import fysom


def code_lines(s):
    fsm = fysom.Fysom(
        {'initial': 'code',
         'events': [
             {'name': 'blockstart', 'src': 'code', 'dst': 'commentblock'},
             {'name': 'blockend', 'src': 'commentblock', 'dst': 'code'},
         ]
         })

    count = 0

    for line in s.split('\n'):
        line = line.strip()

        if '/*' in line and '*/' not in line:
            try:
                fsm.blockstart()
            except fysom.FysomError:
                # already in block, ignore
                pass
        elif fsm.isstate('commentblock') and '*/' in line:
            fsm.blockend()
        elif not line.startswith('//') and len(line) > 0 and fsm.isstate('code'):
            count += 1

    return count
