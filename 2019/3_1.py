n = int(input())
(*a,) = map(int, input().split())
a.sort()
print(min(a[i + n] - a[i] for i in range(n)))
