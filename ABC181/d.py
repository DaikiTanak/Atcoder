# X,Y,A,B = list(map(int, input().split()))

import sys
from collections import defaultdict
import copy
S = input()
# N, M = map(int(input().split()))

num_set = defaultdict(int)

for s in S:
    num_set[s] += 1

# しも三桁が8の倍数かどうかをチェックすればよい

if len(S) < 3:

    for i in range(8, 100, 8):
        num_set_cp = copy.copy(num_set)
        num_str = str(i)
        flag = True
        for s in num_str:
            if num_set_cp[s] > 0:
                num_set_cp[s] -= 1
            else:
                flag = False
        if flag:
            print("Yes")
            sys.exit(0)
        else:
            continue
    print("No")

else:


    for i in range(8, 1000, 8):
        num_set_cp = copy.copy(num_set)
        num_str = str(i)
        while len(num_str) < 3:
            num_str = num_str + "0"
        flag = True
        for s in num_str:
            if num_set_cp[s] > 0:
                num_set_cp[s] -= 1
            else:
                flag = False
        if flag:
            print("Yes")
            sys.exit(0)
        else:
            continue


    print("No")