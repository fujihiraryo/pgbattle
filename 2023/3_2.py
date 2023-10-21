mod = 998244353
n = int(input())
x = input()
if x[0] == "0":
    cnt = 1
    for i in range(1, n):
        if x[i] == "0":
            cnt += 1
        if x[i] == "1":
            break
    for j in range(i, n):
        if x[j] == "0":
            print(0)
            exit()
    print(pow(2, cnt, mod))
else:
    cnt = 1
    for i in range(1, n):
        if x[i] == "1":
            cnt += 1
        if x[i] == "0":
            break
    for j in range(i, n):
        if x[j] == "1":
            print(0)
            exit()
    print(pow(2, cnt, mod))
