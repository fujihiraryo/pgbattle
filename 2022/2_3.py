n = int(input())
(*a,) = map(int, input().split())
stack = []
for x in a[::-1]:
    if x == 1:
        y = 1
        while stack:
            if stack[-1] == y + 1:
                y = stack.pop()
            else:
                break
    else:
        stack.append(x)
print(sum(stack))
