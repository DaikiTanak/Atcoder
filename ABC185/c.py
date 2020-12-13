L = int(input())
# S = input()
# a_li = list(map(int, input().split()))
# N, M = map(int, input().split())
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ans = combinations_count(L-1, 11)
print(ans)