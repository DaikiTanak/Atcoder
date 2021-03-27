N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
# N, M = map(int, input().split())

list_balls = []
list_cost = []

from collections import defaultdict

dict_balls = defaultdict(list)

for _ in range(N):
    x, cost = map(int, input().split())
    list_balls.append({"x":x, "c": cost})
    dict_balls[cost].append(x)

ans = 0
current_x = 0
for cost, list_x in dict_balls.items():
    diffs = [abs(current_x - x) for x in list_x]

    _, list_x = zip(*sorted(zip(diffs, list_x)))


