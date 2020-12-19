N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
# N, M = map(int, input().split())

ans = 0
for i in range(N+1):
    a_flag = False
    b_flag = False
    if "7" in oct(i):
        ans += 1
        a_flag = True
    elif "7" in str(i):
        ans += 1
        b_flag = True


    if a_flag and b_flag:
        ans -= 1
print(N - ans)

