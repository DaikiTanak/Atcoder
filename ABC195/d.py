# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
N, M, Q = map(int, input().split())

li_w = []
li_v = []

for i in range(N):
    w, v = map(int, input().split())
    li_w.append(w)
    li_v.append(v)

li_bag = list(map(int, input().split()))

for i in range(Q):
    l, r = map(int, input().split())
    dp = [0] * 0