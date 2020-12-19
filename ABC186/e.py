T = int(input())
# S = input()
# a_li = list(map(int, input().split()))

ans_list = []
for _ in range(T):
    N, S, K = map(int, input().split())
    residual = N % K
    if residual == 0:
        if (N - K) % S:
            ans_list.append((N-K)//S)
        else:
            ans_list.append(-1)
    else:
        max_ = K * N
        for i in range(1, max_+1):
            if (i - S) % K == 0:
                ans_list.append((i - S) // K)
                break


print(ans_list)

