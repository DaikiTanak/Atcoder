# X,Y,A,B = list(map(int, input().split()))
N = int(input())
# N, M = map(int(input().split()))
# X,Y,A,B = list(map(int, input().split()))
# N = int(input())
# N, M = map(int(input().split()))


a_li = list(map(int, input().split()))

save = {}
maxi = (-1, -1)
for i in range(2, 1001):
    save[i] = 0
    for a in a_li:
        if a % i == 0:
            save[i] += 1
    if maxi[0] < save[i]:
        maxi = (save[i], i)

print(maxi[1])


