# S = input()
# a_li = list(map(int, input().split()))
N, X = map(int, input().split())
S = input()

for result in S:
    if result == "o":
        X += 1
    else:
        X = max(X-1, 0)
print(int(X))


