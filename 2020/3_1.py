n = int(input())
tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
children = [[] for i in range(n)]
visited = [False] * n


stack = [0]
while stack:
    x = stack.pop()
    visited[x] = True
    for y in tree[x]:
        if visited[y]:
            continue
        children[x].append(y)
        stack.append(y)


ans = 0
for x in range(n):
    if not children[x]:
        ans += 1
print(ans)
