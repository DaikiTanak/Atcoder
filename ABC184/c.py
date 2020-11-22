# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

import sys

if r1 == r2 and c1 == c2:
    print(0)
    sys.exit(0)


if (r1 + c1) % 2 == (r2 + c2) % 2:
    # 高々2回の移動でよい
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
        # 同一直線状にいる
        print(1)
        sys.exit(0)
    elif abs(r1 - r2) + abs(c1 - c2) <= 3:
        # 近傍点
        print(1)
        sys.exit(0)
    else:
        # 同一直線状でないかつ近傍でない
        print(2)
        sys.exit(0)
else:
    # 1回以上3回以下の移動が必要
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        sys.exit(0)
    else:
        nearest_x = int(0.5 * ((r1 + r2) + (c1 - c2) - 1))
        nearest_y = r1+c1 - nearest_x
        # print(nearest_x, nearest_y)
        if abs(nearest_x - r2) + abs(nearest_y - c2) <= 3 or abs(nearest_x + 1 - r2) + abs(nearest_y - 1 - c2) <= 3:
            print(2)
            sys.exit(0)

        nearest_x = int(0.5 * ((r1 + r2) + (- c1 + c2) - 1))
        nearest_y = - r1 + c1 + nearest_x
        # print(nearest_x, nearest_y)
        if abs(nearest_x - r2) + abs(nearest_y - c2) <= 3 or abs(nearest_x + 1 - r2) + abs(nearest_y + 1 - c2) <= 3:
            print(2)
            sys.exit(0)

    print(3)
    sys.exit(0)


