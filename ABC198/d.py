# N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
# N, M = map(int, input().split())
S1 = input()
S2 = input()
S3 = input()

# アルファベット割当をA~Jへ限定
# 0 ~ 9のいずれか
set_alphabets = set()
for s in S1+S2+S3:
    set_alphabets.add(s)

set_alphabets = list(set_alphabets)
alphabets = "abcdefghij"
mapping = {}
for idx, a in enumerate(set_alphabets):
    mapping[a] = alphabets[idx]

# transform
S1_ = ""
for s in S1:
    S1_ = S1_ + mapping[s]
S2_ = ""
for s in S2:
    S2_ = S2_ + mapping[s]
S3_ = ""
for s in S3:
    S3_ = S3_ + mapping[s]
print(S1_, S2_, S3_)