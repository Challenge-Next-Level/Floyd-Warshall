import sys

N, C = map(int, sys.stdin.readline().split())
coordinate = []
for _ in range(N):
    coordinate.append(int(sys.stdin.readline().split()[0]))
coordinate.sort()


def install_wifi(distance):
    current = coordinate[0]
    cnt = 1
    for i in range(1, N):
        if coordinate[i] >= current + distance:
            current = coordinate[i]
            cnt += 1
    return cnt


left, right = 0, N - 1
while left <= right:
    mid = (left + right) // 2
    count = install_wifi(mid)
    if count < C:
