N, K = input().split()
N = int(N)
K = int(K)

l_list, r_list = [], []

for k in range(K):
    l_k, r_k = input().split()
    l_k = int(l_k)
    r_k = int(r_k)
    l_list.append(l_k)
    r_list.append(r_k)
# 現在マス 1にいて、後述の方法で移動を繰り返してマス Nへ行こうとしています。
# DPを累積わで高速化する

import numpy as np

dp = np.zeros(N+1)
dp[1] = 1
dpsum = np.zeros(N+1)
dpsum[1] = 1

for i in range(2, N+1):
    for l, r in zip(l_list, r_list):
        li = i - r
        ri = i - l

        ri = max(ri, 0)
        li = max(li, 0)

        dp[i] += dpsum[ri] - dpsum[li-1]

    dpsum[i] = dpsum[i-1] + dp[i]

print(int(dp[N]) % 998244353)







# [EOF]
