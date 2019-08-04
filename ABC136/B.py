
# S = input()
N = input()
# v = map(int, input().split())

n = int(N)

keta = len(N)

if keta == 1:
    print(n)
elif keta == 2:
    print(9)
elif keta == 3:
    print(9 + n - 99)
elif keta == 4:
    print(909)
elif keta == 5:
    print(909 + n - 9999)
elif keta == 6:
    print(90909)
