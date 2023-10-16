import math

n = int(input())

print(math.ceil(sum(math.log10(i) for i in range(1, n + 1))))
