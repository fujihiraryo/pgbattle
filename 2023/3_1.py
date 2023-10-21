a, b, c, d, l, r = map(int, input().split())


def f(x):
    return a * x**3 + b * x**2 + c * x + d


if f(l) == 0:
    print(l)
    exit()

if f(r) == 0:
    print(r)
    exit()

if f(l) > 0 and f(r) < 0:
    while r - l > 10 ** (-8):
        m = (l + r) / 2
        if f(m) < 0:
            r = m
        else:
            l = m
else:
    while r - l > 10 ** (-8):
        m = (l + r) / 2
        if f(m) < 0:
            l = m
        else:
            r = m
print(l)
