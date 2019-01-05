import attr


@attr.s
class Simple:
    value = attr.ib()
    label = attr.ib()


@attr.s
class Defaults:
    value = attr.ib(default=17)
    label = attr.ib(default='baz')


@attr.s(frozen=True)
class Frozen:
    value = attr.ib()
    label = attr.ib()


@attr.s(frozen=True)
class FrozenDefaults:
    x = attr.ib(default=17)


@attr.s
class NoInitNoDefault:
    y = attr.ib(init=False)


@attr.s
class NoInit:
    y = attr.ib(init=False, default=888)


@attr.s
class Factoried:
    d = attr.ib(factory=Defaults)


@attr.s
class FactoriedWithArgs:
    la = attr.ib()
    va = attr.ib()
    d = attr.ib()

    @d.default
    def simple_factory(self):
        return Simple(value=self.va, label=self.la)


@attr.s
class Typed:
    i = attr.ib(type=int)
    s = attr.ib(type=str)


@attr.s
class TypedValidated:
    i = attr.ib(type=int)

    @i.validator
    def check_i(self, attribute, value):
        assert type(value) == attribute.type
