import attr
import pytest

from attrs20190107 import experiments


class TestExperiments:

    def test_derived_default(self):
        o = experiments.DerivedDefault(x=1)
        assert o.x == 1
        assert o.s == '000001'

        # default doesn't update when x is updated
        o.x = 5
        assert o.s == '000001'

        # default also doesn't update with evolve
        p = attr.evolve(o, x=17)
        assert p.s == '000001'

    def test_set_via_validator(self):
        o = experiments.SetViaValidator(x=1)
        assert o.x == 1
        assert o.s == '000001'

        # validator is not re-run when setting attribute value
        o.x = 5
        assert o.s == '000001'

    def test_set_via_formatter(self):
        o = experiments.SetViaFormatter(x=1)
        assert o.x == 1
        assert o.x_s == 'n.a.'

        experiments.obj_formatter(o)
        assert o.x == 1
        assert o.x_s == '000001'

    def test_get_via_property(self):
        o = experiments.GetViaProperty(x=1)
        assert o.x == 1
        assert o.x_s == '000001'

        with pytest.raises(AttributeError):
            # noinspection PyPropertyAccess
            o.x_s = 'n.a.'

        # propertie don't show up in dicts!
        assert 'x' in attr.asdict(o)
        assert 'x_s' not in attr.asdict(o)

    def test_set_via_evolve_multi(self):
        o = experiments.SetViaEvolveMulti(x=1)
        assert o.x == 1
        assert o.x_s == '000001'

        with pytest.raises(attr.exceptions.FrozenInstanceError):
            # noinspection PyDataclass
            o.x = 13

        p = experiments.evolve_multi(o, x=17)
        assert p.x == 17
        assert p.x_s == '000017'

    def test_set_via_evolve_multi_better(self):
        o = experiments.SetViaEvolveMultiBetter(x=1, p=0.01)
        assert o.x == 1
        assert o.x_s == '000001'
        assert o.p_s == '0.01%'

        with pytest.raises(attr.exceptions.FrozenInstanceError):
            # noinspection PyDataclass
            o.x = 13

        p = experiments.evolve_multi(o, x=17, p=13.1234)
        assert p.x == 17
        assert p.x_s == '000017'
        assert p.p_s == '13.12%'
