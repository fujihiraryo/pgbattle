def max_ans(n, m):
    l = 0
    r = 10**10
    while r - l > 1:
        c = (l + r) // 2
        if m <= c * (c - 1) // 2:
            r = c
        else:
            l = c
    return n - r + 1


def min_ans(n, m):
    return max(1, n - m)


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(min_ans(n, m), max_ans(n, m))
