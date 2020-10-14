H, W = list(map(int, input().split()))

former_row = 0
this_row = 0

def count_this_row(strings):
    count = 0
    for i, s in enumerate(strings):
        if i > 0 and (s == "." and strings[i-1] == "."):
            count += 1
    return count


counter = 0
for i in range(H):
    this_row = input()
    counter += count_this_row(this_row)

    if i > 0:
        for j in range(W):
            if this_row[j] == former_row[j] == ".":
                counter += 1

    former_row = this_row



print(counter)
