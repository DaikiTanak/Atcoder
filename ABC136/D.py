S = input()

L_searching_flag = True
R_searching_flag = False
LR_idx = []
boundary_idx = []
for i, char in enumerate(S):
    if L_searching_flag:
        if char == "L":
            L_searching_flag = False
            R_searching_flag = True
            LR_idx.append(i)
        else:
            continue
    elif R_searching_flag:
        if char == "R":
            L_searching_flag = True
            R_searching_flag = False
            boundary_idx.append(i - 1)
        else:
            continue

# dummy right side idx
boundary_idx.append(len(S)-1)

last_right_L = -1

ans = []
for left_L_idx, right_L_idx in zip(LR_idx, boundary_idx):
    while(len(ans) < left_L_idx-1):
        ans.append(str(0))


    L_num = right_L_idx - left_L_idx + 1
    R_num = left_L_idx - last_right_L - 1
    last_right_L = right_L_idx
    if (L_num + R_num) % 2 == 0:
        ans.append(str(int((L_num+R_num)/2)))
        ans.append(str(int((L_num+R_num)/2)))
    else:
        if R_num < L_num:
            if L_num % 2 == 1:
                ans.append(str(int((L_num+R_num-1)/2)))
                ans.append(str(int((L_num+R_num+1)/2)))
            else:
                ans.append(str(int((L_num+R_num+1)/2)))
                ans.append(str(int((L_num+R_num-1)/2)))
        else:
            if R_num % 2 == 1:
                ans.append(str(int((L_num+R_num+1)/2)))
                ans.append(str(int((L_num+R_num-1)/2)))
            else:
                ans.append(str(int((L_num+R_num-1)/2)))
                ans.append(str(int((L_num+R_num+1)/2)))

while(len(ans) < len(S)):
    ans.append(str(0))

print(" ".join(ans))
