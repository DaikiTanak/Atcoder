import numpy as np
N = int(input())
# S = input()
# a_li = sorted(list(map(int, input().split())))
a_li = (list(map(int, input().split())))
# N, M = map(int, input().split())

cumsum = [a_li[0]]
for idx, a in enumerate(a_li):
    if idx > 0:
        cumsum.append(a + cumsum[-1])

square_a_li = np.array(a_li) ** 2
square_sum = np.sum(square_a_li) * (N - 1)

minus = 0
for idx, a in enumerate(a_li[-1::-1][:-1]):
    minus += a * cumsum[-(idx+2)]

print(square_sum - 2 * minus)