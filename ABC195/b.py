# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
A, B, W = map(int, input().split())

sum_gram = W*1000

lower_bound = sum_gram // B if sum_gram % B == 0 else (sum_gram // B) + 1
upper_bound = sum_gram // A

if upper_bound == 0 or lower_bound > upper_bound:
    print("UNSATISFIABLE")
else:
    print(f"{lower_bound} {upper_bound}")