n = int(input())
s = input()
l0 = 0
r0 = n + 1
l1 = 0
r1 = n + 1
used = [0] * (n + 2)
for c in s:
    sit = False
    if c == "L":
        for i in range(l0 + 1, r0):
            if used[i - 1] == 0 and used[i] == 0 and used[i + 1] == 0:
                print(i)
                used[i] = 1
                l0 = i
                sit = True
                break
    else:
        for i in range(l0 + 1, r0)[::-1]:
            if used[i - 1] == 0 and used[i] == 0 and used[i + 1] == 0:
                print(i)
                used[i] = 1
                r0 = i
                sit = True
                break
    if sit:
        continue
    if c == "L":
        for i in range(l1 + 1, r1):
            if used[i] == 0:
                print(i)
                used[i] = 1
                l1 = i
                break
    else:
        for i in range(l1 + 1, r1)[::-1]:
            if used[i] == 0:
                print(i)
                used[i] = 1
                r1 = i
                break
