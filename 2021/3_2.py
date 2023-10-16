n, s = map(int, input().split())
d = list(map(int, input().split()))
min_s = sum(pow(10, d[i] - 1) for i in range(n))
max_s = sum(pow(10, d[i]) - 1 for i in range(n))
if s < min_s or max_s < s:
    print(-1)
    exit()
ans = [pow(10, d[i] - 1) for i in range(n)]
ans_sum = sum(ans)
for i in range(n):
    if ans_sum < s:
        x = min(s - ans_sum, pow(10, d[i]) - 1 - ans[i])
        ans[i] += x
        ans_sum += x
print(*ans)
