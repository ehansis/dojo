from . import dependencies


def test_add():
    d = dependencies.Dep()
    d.add('A', ['B', 'C'])
    d.add('B', ['C'])
    d.add('A', ['C'])
    d.add('A', ['D'])

    assert len(d.dep_map) == 2
    assert d.dep_map['A'] == {'B', 'C', 'D'}
    assert d.dep_map['B'] == {'C'}


def test_deps_1():
    dep = dependencies.Dep()
    dep.add('A', ['B', 'C'])
    dep.add('B', ['C', 'E'])
    dep.add('C', ['G'])
    dep.add('D', ['A', 'F'])
    dep.add('E', ['F'])
    dep.add('F', ['H'])

    assert {'B', 'C', 'E', 'F', 'G', 'H'} == dep.deps('A')
    assert {'C', 'E', 'F', 'G', 'H'} == dep.deps('B')
    assert {'G'} == dep.deps('C')
    assert {'A', 'B', 'C', 'E', 'F', 'G', 'H'} == dep.deps('D')
    assert {'F', 'H'} == dep.deps('E')
    assert {'H'} == dep.deps('F')


def test_deps_2():
    dep = dependencies.Dep()
    dep.add('A', ['B'])
    dep.add('B', ['C'])
    dep.add('C', ['A'])

    assert {'B', 'C'} == dep.deps('A')
    assert {'C', 'A'} == dep.deps('B')
    assert {'A', 'B'} == dep.deps('C')
