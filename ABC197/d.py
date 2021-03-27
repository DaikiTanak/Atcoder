import numpy as np

N = int(input())
# S = input()
# a_li = list(map(int, input().split()))
x0, y0 = map(int, input().split())
x_half, y_half = map(int, input().split())

rotate_angle = -np.radians([360 / N])[0]

center_x = (x0 + x_half) / 2
center_y = (y0 + y_half) / 2


x0_relative = x0 - center_x
y0_relative = y0 - center_y

rotation_matrix = np.array([
    [np.cos(rotate_angle), -np.sin(rotate_angle)],
    [np.sin(rotate_angle), np.cos(rotate_angle)]
])

x1_relative, y1_relative = np.array([x0_relative, y0_relative]) @ rotation_matrix
x1 = x1_relative + center_x
y1 = y1_relative + center_y

print(f"{x1} {y1}")

