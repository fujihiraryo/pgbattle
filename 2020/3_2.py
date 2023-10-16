def ans(n, s, x):
    # 長さn,和がs,最初がx
    if n == 1:
        if x == s:
            yield [s]
        return
    for y in range(x, s + 1):
        for lst in ans(n - 1, s - x, y):
            yield [x] + lst


n, s = map(int, input().split())
for x in range(1, s + 1):
    for lst in ans(n, s, x):
        print(*lst)
