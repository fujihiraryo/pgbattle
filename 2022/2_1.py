n, q = map(int, input().split())
lst = [0] * n
for _ in range(q):
    l, r = map(int, input().split())
    for x in range(l - 1, r):
        lst[x] ^= 1
print(sum(lst))
