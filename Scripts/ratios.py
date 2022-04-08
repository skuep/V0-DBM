from fractions import Fraction

pulleys = range(22, 33)
limits = range(2, 9)

print(f'pulleys: {list(pulleys)}')
print(f'limits: {list(limits)}')

for a_pulley in pulleys:
    for b_pulley in pulleys:
        for c_pulley in pulleys:
            for d_pulley in pulleys:
                try:
                    a = Fraction(a_pulley, b_pulley)
                    b = Fraction(c_pulley, d_pulley)
                    d = 2/(1 - a * b)
                    r = float(d)
                    if r.is_integer() and int(r) in limits:
                        print(f'[{a_pulley}/{b_pulley}, {c_pulley}/{d_pulley}: {r}')
                except Exception:
                    pass


