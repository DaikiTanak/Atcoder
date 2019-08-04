import sys

N = int(input())
h_list = list(map(int, input().split()))

max_up = -1
max_down = 1

if h_list[0] > 1:
    h_list[0] -= 1

for i in range(len(h_list[:-1])):

    h = h_list[i]
    next_h = h_list[i+1]
    diff = next_h - h

    if diff > 0:
        h_list[i+1] = next_h - 1
    elif diff < 0:
        print("No")
        sys.exit()
print("Yes")
