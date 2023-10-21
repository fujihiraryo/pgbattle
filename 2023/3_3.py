mod = 998244353
n, m = 10**5, 10**2
s = "1" * n
dp = [[0] * m for _ in range(n + 1)]
dp[1][int(s[0]) % m] = 1
for i in range(1, n):
    for j in range(m):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= mod
        dp[i + 1][(10 * j + int(s[i])) % m] += dp[i][j]
        dp[i + 1][(10 * j + int(s[i])) % m] %= mod
    dp[i + 1][int(s[i]) % m] += 1
    dp[i + 1][int(s[i]) % m] %= mod
print(dp[n][0])
