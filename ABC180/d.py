X,Y,A,B = list(map(int, input().split()))


# X: 始めの強さ
# Y: 強さをY未満となるように
# A: X_new = X_old * A
# B: X_new = X_old + B
# カコモンジムに何度か通い、その後AtCoderジムに何度か通うのが最適解になります。


exp = 0
X_now = X

while X_now * A < X_now + B and X_now * A < Y:
    X_now = X_now * A
    exp += 1

print(exp + (Y - 1 - X_now) // B)
