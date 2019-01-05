import attr
import pytest

from attrs20190105 import experiments


class TestExperiments:

    def test_simple(self):
        o = experiments.Simple(value=1, label='foo')
        assert o.label == 'foo'
        assert o.value == 1

        o.label = 'bar'
        o.value = 42

        print(o)

        assert attr.asdict(o) == dict(value=42, label='bar')

    def test_defaults(self):
        o = experiments.Defaults()
        assert o.label == 'baz'
        assert o.value == 17

    def test_frozen(self):
        o = experiments.Frozen(value=5, label='zit')

        with pytest.raises(attr.exceptions.FrozenInstanceError):
            # noinspection PyDataclass
            o.label = 9

    def test_frozen_defaults(self):
        o = experiments.FrozenDefaults()
        assert o.x == 17

        p = experiments.FrozenDefaults(x=23)
        assert p.x == 23

    def test_noinitnodefault(self):
        o = experiments.NoInitNoDefault()

        with pytest.raises(AttributeError):
            print(o.y)

        with pytest.raises(TypeError):
            # noinspection PyArgumentList
            experiments.NoInitNoDefault(y=1)

    def test_noinit(self):
        o = experiments.NoInit()
        assert o.y == 888

        with pytest.raises(TypeError):
            # noinspection PyArgumentList
            experiments.NoInitNoDefault(y=1)

    def test_factoried(self):
        o = experiments.Factoried()
        assert o.d.value == 17

    def test_factoriedwithargs(self):
        o = experiments.FactoriedWithArgs(la='yep', va=3.141)
        assert o.d.label == 'yep'
        assert o.d.value == 3.141

    def test_typed(self):
        o = experiments.Typed(i=3, s='abc')
        assert o.i == 3
        assert o.s == 'abc'

        # attrs doesn't do any type checking itself!
        o.s = 17
        assert type(o.s) == int

        p = experiments.Typed(i=(0.1, 0.2), s=None)
        assert p.s is None

    def test_typedvalidated(self):
        experiments.TypedValidated(i=5)

        with pytest.raises(AssertionError):
            experiments.TypedValidated(i='foo')
