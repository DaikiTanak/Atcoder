import math
# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
R, X, Y = map(int, input().split())

squared_dis = X**2 + Y**2
dis = math.sqrt(squared_dis)

if dis < R:
    # 近すぎる場合は2回かけないと行けない
    print(2)
else:
    print(int(math.ceil(dis / R)))

