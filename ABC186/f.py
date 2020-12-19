# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
import numpy as np
H, W, M = map(int, input().split())
grids = np.zeros((H, W))

for i in range(M):
    x, y = map(int, input().split())
    # grids[x-1][y-1] = - (4*10**5)
    grids[x-1][y-1] = - 1

for idx1, row in enumerate(grids):
    for idx2, col in enumerate(row):
        if idx1 == 0 or idx2 == 0:
            continue

        target = grids[idx1][idx2]
        if target == -1:

            grids[idx1:][idx2] = - 1e+50
            grids[idx1][idx2:] = - 1e+50
            

ans = 0
for element in grids.flatten():
    if 1<= element <= 2:
        ans += 1

print(grids)
print(int(ans))