n = int(input())
(*a,) = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for p in range(n + 1):
    for i in range(2**n):
        if a[i] == 2**p:
            lst[p].append(i + 1)
if len(lst[0]) != 1 or any(len(lst[i]) != 2 ** (i - 1) for i in range(1, n + 1)):
    print(-1)
    exit()
ans = [None] * 2**n
idx = 0
for i in range(n + 1):
    for x in lst[i]:
        ans[idx] = x
        if idx < 2**n // 2:
            idx = 2**n - 1 - idx
        else:
            idx = 2**n - idx
print(*ans)
