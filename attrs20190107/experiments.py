import attr
from functools import partial


@attr.s
class DerivedDefault:
    x = attr.ib()
    s = attr.ib()

    @s.default
    def x_to_str(self):
        return "{:06d}".format(self.x)


@attr.s
class SetViaValidator:
    x = attr.ib()
    s = attr.ib(default='n.a.')

    @x.validator
    def x_val(self, attribute, value):
        self.s = "{:06d}".format(value)
        return True


@attr.s
class SetViaFormatter:
    x = attr.ib()
    x_s = attr.ib(default='n.a.')


def obj_formatter(obj):
    for a in attr.fields(obj.__class__):
        if hasattr(obj, a.name + '_s'):
            setattr(obj, a.name + '_s', '{:06d}'.format(getattr(obj, a.name)))


@attr.s
class GetViaProperty:
    x = attr.ib()

    @property
    def x_s(self):
        return '{:06d}'.format(self.x)


def _int_formatter(i):
    return "{:06d}".format(i)


UPDATES_ON_KEY = 'UPDATES_ON'
FORMATTER_KEY = 'FORMATTER'


def evolve_multi(obj, **kwargs):
    for a in attr.fields(obj.__class__):
        updates_on = a.metadata.get(UPDATES_ON_KEY, '')
        if updates_on in kwargs.keys():
            kwargs[a.name] = a.metadata[FORMATTER_KEY](kwargs[updates_on])
    new_obj = attr.evolve(obj, **kwargs)
    return new_obj


@attr.s(frozen=True)
class SetViaEvolveMulti:
    x = attr.ib()
    x_s = attr.ib(default=attr.Factory(
        lambda obj: _int_formatter(getattr(obj, 'x')), takes_self=True),
        metadata={'UPDATES_ON': 'x', 'FORMATTER': _int_formatter})


def updates(updates_on, formatter, validator=None, repr=True,
            cmp=True, hash=None, init=True, convert=None, metadata=None):
    metadata = dict() if metadata is None else metadata
    metadata[UPDATES_ON_KEY] = updates_on
    metadata[FORMATTER_KEY] = formatter
    return attr.ib(validator=validator, repr=repr, cmp=cmp, hash=hash, init=init, convert=convert,
                   metadata=metadata,
                   default=attr.Factory(lambda obj: formatter(getattr(obj, updates_on)), takes_self=True))


def _percent_formatter(f):
    return "{:.2f}%".format(f)


@attr.s(frozen=True)
class SetViaEvolveMultiBetter:
    x = attr.ib()
    p = attr.ib()

    x_s = updates('x', _int_formatter)
    p_s = updates('p', _percent_formatter)
