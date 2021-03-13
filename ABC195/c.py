N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
# N, M = map(int, input().split())

current_num_comma = (len(str(N)) - 1) // 3

ans = 0

for num_comma in range(1, current_num_comma):
    ans += ((10 ** ((num_comma + 1) * 3) - 1) - ((10 ** (num_comma * 3)) - 1)) * num_comma

ans += current_num_comma * (N - ((10 ** (current_num_comma * 3)) - 1))

print(ans)
