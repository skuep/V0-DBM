from fractions import Fraction
from typing import Iterable, NamedTuple

class BeltRatio(NamedTuple):
    a: int
    b: int
    c: int
    d: int

    @property
    def pulleys(self) -> Iterable[Fraction]:
        return (Fraction(self.a, self.b), Fraction(self.c, self.d))

    @property
    def ma(self) -> Fraction:
        return 2 / (1 - self.pulleys[0] * self.pulleys[1])

    def __eq__(self, other):
        me = self.pulleys
        you = other.pulleys
        return True if (me == you) or (me == you[::-1]) else False

    def __str__(self):
        return f'1:{self.ma} [{self.a}/{self.b}{"*" if self.a==self.b else ""}, {self.c}/{self.d}{"*" if self.c==self.d else ""}]'

pulleys = range(24, 33)
limits = [2, 4, 5, 8, 10, 16, 20]

print(f'pulleys: {list(pulleys)}')
print(f'limits: {list(limits)}')

ratios = []

for a in pulleys:
    for b in pulleys:
        for c in pulleys:
            for d in pulleys:
                try:
                    o = BeltRatio(a, b, c, d)
                    r = float(o.ma)
                    if r.is_integer() and int(r) in limits and o not in ratios:
                        ratios.append(o)
                except Exception:
                    pass

ratios.sort( key=lambda a: a.ma )

for ratio in ratios:
    print(ratio)

