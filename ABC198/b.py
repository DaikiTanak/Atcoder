import sys
N = str(input())
# S = input()
# a_li = list(map(int, input().split()))
# N, M = map(int, input().split())

count_tail_zero = 0
for idx, s in enumerate(N[-1::-1]):
    if s == "0":
        count_tail_zero += 1
    else:
        break

N_ = "0" * count_tail_zero + N
half_idx = len(N_) // 2
for idx, s in enumerate(N_):
    if idx == half_idx:
        break
    if N[-(idx+1)] == s:
        pass
    else:
        print("No")
        sys.exit(0)

print("Yes")