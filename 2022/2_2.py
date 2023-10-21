n = int(input())
(*a,) = map(int, input().split())
lst = [(a[i], i + 1) for i in range(3 * n)]
lst.sort()
idx = []
for _, i in lst[n : 2 * n]:
    idx.append(i)
idx.sort()
print(*idx, sep="\n")
