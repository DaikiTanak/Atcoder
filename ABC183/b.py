# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
s_x, s_y, g_x, g_y = map(int, input().split())

print(((s_y / (s_y + g_y)) * (g_x - s_x)) + s_x)
