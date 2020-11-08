# X,Y,A,B = list(map(int, input().split()))
N = int(input())
# N, M = map(int(input().split()))
a_li = list(map(int, input().split()))
#N = int(input())
# N, M = map(int(input().split()))

cusum_forward = 0
max_pos = - 10 ** 9
ending_pos = 0
previous_pos = 0
max_pos = 0
cusum_save = [0] * N
max_cusum = -10 ** 9

for idx, a in enumerate(a_li):
    if idx > 0:
        cusum_save[idx] = cusum_save[idx-1] + a
    else:
        cusum_save[idx] = a

    # 今回の着地座標
    ending_pos += cusum_save[idx]
    max_cusum = max(max_cusum, cusum_save[idx])
    max_pos_this = previous_pos + max_cusum

    if max_pos < max_pos_this:
        max_pos = max_pos_this

    previous_pos = ending_pos

print(max_pos)




