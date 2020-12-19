# N = int(input())
# S = input()
H, W = map(int, input().split())

a = []
for i in range(H):
    a_li = list(map(int, input().split()))
    a.extend(a_li)

min_a = min(a)
print(sum(a) - min_a * H * W)