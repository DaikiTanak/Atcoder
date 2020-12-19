import numpy as np

N = int(input())
# S = input()
# 降順ソート
a_li = sorted(list(map(int, input().split())))[-1::-1]
# N, M = map(int, input().split())


ans = 0
for idx1, a1 in enumerate(a_li):
    ans += a1 * (N-1-idx1) - idx1 * a1

print(ans)