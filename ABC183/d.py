def main():
    import sys
    import numpy as np
    from sys import stdin
    readline = stdin.readline
    N, W = map(int, readline().split())

    amounts = dict()

    for i in range(N):
        si, ti, pi = map(int, input().split())
        for t in range(si, ti):
            try:
                amounts[t] += pi
            except KeyError:
                amounts[t] = pi

    for a in amounts.values():
        if a > W:
            print("No")
            sys.exit(0)

    print("Yes")

main()