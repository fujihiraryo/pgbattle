def cand(t):
    s = set()
    for x in range(0, t + 1):
        y = int((t**2 - x**2) ** 0.5)
        if x**2 + y**2 == t**2:
            s |= {(x, y), (-x, y), (x, -y), (-x, -y)}
            s |= {(y, x), (-y, x), (y, -x), (-y, -x)}
    return s


w, h, t = map(int, input().split())
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
ans = 0
for dx, dy in cand(t):
    x = sx + dx
    y = sy + dy
    xCond = (x // w % 2 == 0 and x % w == tx) or (x // w % 2 == 1 and x % w == w - tx)
    yCond = (y // h % 2 == 0 and y % h == ty) or (y // h % 2 == 1 and y % h == h - ty)
    if xCond and yCond:
        ans += 1
print(ans)
