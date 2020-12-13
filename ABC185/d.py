# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
import sys
N, M = map(int, input().split())
a_li = sorted(list(map(int, input().split())))

if N == M:
    print(0)
    sys.exit(0)

elif M == 0:
    print(1)
    sys.exit(0)


a_li = [0] + a_li + [N+1]
diff_list = []
for i, a in enumerate(a_li):
    try:
        add = a_li[i+1] - a - 1
        if add > 0:
            diff_list.append(add)
    except Exception as e:
        # print(e)
        pass

# print(diff_list)

ans = 0
k = min(diff_list)
for diff in diff_list:
    if diff % k == 0:
        ans += (diff // k)
    else:
        ans += (diff // k) + 1

print(ans)