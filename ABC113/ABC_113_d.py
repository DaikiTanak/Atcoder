import numpy as np


# A(h, x) を、上から h 行目を通過した (横棒を通った場合も含む) 直後に左から x 本目の縦棒に
# いる場合の数とします


H, W, K = map(int, input().split())
print(H,W,K)

A = np.zeros(shape=(H+1,W))
A[0][0] = 1
print(A)

num = np.zeros(shape=(W,W))
for w in range(W):
    bit = bin(w)
    str_bit = str(bit)
    for c in range(len(str_bit)):
        if w[c] == 1 and w[c+1] == 1:
            num[]

for i in range(1, H+1, 1):
    for j in range(W):
        if j == 0:
            A[i][j] = A[i-1][j]
