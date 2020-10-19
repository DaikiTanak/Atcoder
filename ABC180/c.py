N = int(input())

ans = []
for i in range(1, int(N**0.5)+1, 1):
    q, mod = divmod(N, i)
    # print(i, q, mod)
    if mod == 0:
        ans.append(i)
        if not i == q:
            ans.append(q)

for a in sorted(ans):
    print(a)
