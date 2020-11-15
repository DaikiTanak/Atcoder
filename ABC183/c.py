import numpy as np

# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
N, K = map(int, input().split())
costs = np.zeros((N, N))

for i in range(N):
    t_li = list(map(int, input().split()))
    costs[i] = np.asarray(t_li)

# 探索候補スタック
stack = [0]
# 探索済リスト
visited = []
nodes = set([i for i in range(N)])


def dfs(current_city_idx, visited, current_costs):
    ans = 0


    visited = visited + [current_city_idx]
    candidates = nodes - set(visited)

    print(current_city_idx, visited, current_costs, candidates)
    if len(candidates) == 0:
        current_costs += costs[current_city_idx][0]
        if current_costs == K:
            return 1
        else:
            return 0

    for city_idx in candidates:
        ans += dfs(city_idx, visited,
                   current_costs + costs[current_city_idx][city_idx])
    return ans

ans = dfs(0, [], 0)
print(ans)
