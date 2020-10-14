import numpy as np
N = int(input())
p_list = list(map(int, input().split()))


existed = {}
current_min = 0

for idx, p in enumerate(p_list):

    existed[p] = True

    if p == current_min:
        q = p + 1
        while True:
            try:
                _ = existed[q]
                q += 1
                continue
            except KeyError:
                current_min = q
                break

    print(current_min)
