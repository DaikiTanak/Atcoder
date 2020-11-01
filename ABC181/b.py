# X,Y,A,B = list(map(int, input().split()))
N = int(input())
# N, M = map(int(input().split()))
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    ans += (a+b)*(b-a+1) / 2


print(int(ans))