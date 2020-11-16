def main():
    import sys
    readline = sys.stdin.readline
    N, W = map(int, readline().split())

    amounts = [0] * (2 * (10**5) + 1)

    for i in range(N):
        si, ti, pi = map(int, input().split())
        amounts[si] += pi
        amounts[ti] -= pi

    cusum = 0
    for a in amounts:
        cusum += a
        if cusum > W:
            print("No")
            sys.exit(0)

    print("Yes")

main()