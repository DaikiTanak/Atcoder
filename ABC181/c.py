import sys

# X,Y,A,B = list(map(int, input().split()))
N = int(input())
# N, M = map(int(input().split()))

x_li, y_li = [], []
for _ in range(N):
    x, y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)


for i, (x1, y1) in enumerate(zip(x_li, y_li)):
    for j, (x2, y2) in enumerate(zip(x_li, y_li)):
        for k, (x3, y3) in enumerate(zip(x_li, y_li)):
            if i < j < k:

                try:
                    grad1 = (y2-y1) / (x2-x1)
                except ZeroDivisionError as e:
                    grad1 = None
                try:
                    grad2 = (y3-y1) / (x3-x1)
                except ZeroDivisionError as e:
                    grad2 = None

                if grad1 == grad2:
                    print("Yes")
                    sys.exit(0)
print("No")