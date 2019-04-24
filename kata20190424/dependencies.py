from collections import defaultdict


class Dep:

    def __init__(self):
        self.dep_map = defaultdict(set)

    def add(self, key, deps):
        self.dep_map[key] |= set(deps)

    def deps(self, key, out=None):
        if out is None:
            out = set()
            final = True
        else:
            final = False

        for k in self.dep_map.get(key, {}):
            if k not in out:
                out.add(k)
                self.deps(k, out)

        # don't list self-references
        if final:
            out -= {key}

        return out
