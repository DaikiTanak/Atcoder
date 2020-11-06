# X,Y,A,B = list(map(int, input().split()))
S = int(input())
# N, M = map(int(input().split()))

ans = 0

dp = [0] * 2001
dp[0] = 1
dp[1] = 0
dp[2] = 0
dp[3] = 1

for n in range(4, S+1, 1):
    dp[n] = dp[n-3] + dp[n-1]

ans = dp[S]
print(int(ans % ((10**9)+7)))
