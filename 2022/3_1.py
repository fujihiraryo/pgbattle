n = int(input())
b = set(map(int, input().split()))
d = (max(b) - min(b)) // n
for x in range(min(b), max(b), d):
    if x not in b:
        print(x)
        exit()
