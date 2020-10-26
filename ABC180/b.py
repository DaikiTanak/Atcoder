N = int(input())
x_list = list(map(int, input().split()))


man = sum(map(abs, x_list))
euc = sum(map(lambda x: abs(x)**2, x_list)) ** 0.5
che = max(map(lambda x: abs(x), x_list))

print(man)
print(euc)
print(che)
