# X,Y,A,B = list(map(int, input().split()))
N = input()
# N, M = map(int(input().split()))
# X,Y,A,B = list(map(int, input().split()))
# N = int(input())
# N, M = map(int(input().split()))

keta_sum = 0
amari3 = {0:0, 1:0, 2:0}
for n in N:
    amari = int(n) % 3
    amari3[amari] += 1
    keta_sum += int(n)

sum_amari3 = keta_sum % 3
ans = 0

if sum_amari3 == 0:
    print(0)
elif sum_amari3 == 1:
    if amari3[1] >= 1:
        # あまり1の数を1つ消せばよい
        if len(N) > 1:
            print(1)
        else:
            print(-1)
    elif amari3[2] >= 2:
        # あまり2の数を2つ消せばよい
        if len(N) > 2:
            print(2)
        else:
            print(-1)
    else:
        print(-1)
elif sum_amari3 == 2:
    if amari3[2] >= 1:
        # あまり2の数を1つ消せばよい
        if len(N) > 1:
            print(1)
        else:
            print(-1)
    elif amari3[1] >= 2:
        # あまり1の数を2つ消せばよい
        if len(N) > 2:
            print(2)
        else:
            print(-1)
    else:
        print(-1)
