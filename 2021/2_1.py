p = int(input())


def frac(x):
    p = 1
    for i in range(1, x + 1):
        p *= i
    return p


def cmb(n, r):
    return frac(n) // frac(n - r) // frac(r)


ans = 0
for i in range(4, 7 + 1):
    ans += cmb(7, i) * (p / 100) ** i * (1 - p / 100) ** (7 - i)
print(ans * 100)
