# 좌우 반전
T = int(input())
for j in range(T):
    h, w = map(int, input().split())
    for i in range(h):
        a = input()
        b = w - 1
        while b >= 0:
            print(a[b], end="")
            b = b - 1
        print()
