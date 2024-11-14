import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, S = input().split()

    R = int(R)

    for s in S:
        print(R * s, end="")
    print()
