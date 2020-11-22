# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
a, b, c = map(int, input().split())

# 99,99,99からスタートして1枚づつ減らして行けば良さそう
# 99,99,99での期待値は1

import numpy as np

dp = np.zeros((101, 101, 101))
dp[99][99][99] = 1
dp[100][100][100] = 0

for i in range(99, 0, -1):
    for j in range(i, 0, -1):
        for k in range(j, 0, -1):
            if i == j == k == 99:
                continue
            else:
                i_, j_, k_ = sorted([i, j, k+1])[-1::-1]

                dp[i][j][k] = dp[i_][j_][k_] + k / (i+j+k)
                # print(i, j, k, dp[i][j][k])
                # input()

a, b, c = sorted([a, b, c])[-1::-1]
print(a,b,c)
print(dp[a][b][c])