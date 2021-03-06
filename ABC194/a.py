# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
a, b = map(int, input().split())



all_ = a + b

if all_ >= 15 and b >= 8:
    print(1)
elif all_ >= 10 and b >= 3:
    print(2)
elif all_ >= 3:
    print(3)
else:
    print(4)