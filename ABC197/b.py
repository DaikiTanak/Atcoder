import numpy as np
# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
h, w, x, y = map(int, input().split())

li_s = [[""] * w] * h
li_s = np.array(li_s)

for idx1 in range(h):
    s = input()
    for idx2, c in enumerate(s):
        li_s[idx1][idx2] = c


ans = 0

row = li_s[x-1, :]
col = li_s[:, y-1]
# print(row, col)

if li_s[x-1, y-1] == "#":
    ans = 1
else:
    for c in row[:y][-1::-1]:
        if c == "#":
            break
        else:
            ans += 1
    for c in row[y:]:
        if c == "#":
            break
        else:
            ans += 1
    for c in col[:x][-1::-1]:
        if c == "#":
            break
        else:
            ans += 1
    for c in col[x:]:
        if c == "#":
            break
        else:
            ans += 1
    # remove double count for center block
    ans -= 1

print(ans)