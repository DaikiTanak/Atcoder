import numpy as np
N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
# N, M = map(int, input().split())


a_li = []
b_li = []
for i in range(N):
    a, b = map(int, input().split())
    a_li.append(a)
    b_li.append(b)

min_a = np.min(a_li)
min_a_idx = np.argmin(a_li)
min_b = np.min(b_li)
min_b_idx = np.argmin(b_li)

if min_a_idx == min_b_idx:

    second_min_a = sorted(a_li)[1]
    second_min_b = sorted(b_li)[1]
    alone = min_a + min_b
    print(min(alone, max(min_a, second_min_b), max(min_b, second_min_a)))

else:
    print(max(min_a, min_b))