# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
import sys
N, M, T = map(int, input().split())

current = N
diff = 0
b_last = 0
for i in range(M):
    a, b = map(int, input().split())

    if i == 0:
        diff = a
    else:
        diff = a - b_last
    b_last = b

    cafe_start = current - diff
    cafe_end = min(cafe_start + (b - a), N)
    # print(i, diff, cafe_start, cafe_end)

    if cafe_start <= 0:
        print("No")
        sys.exit(0)

    current = cafe_end

last = current - (T - b_last)
# print(last)

if last <= 0:
    print("No")
else:
    print("Yes")