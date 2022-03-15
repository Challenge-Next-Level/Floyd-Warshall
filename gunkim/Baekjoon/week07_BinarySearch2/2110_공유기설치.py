import sys

N, C = map(int, sys.stdin.readline().split()) # 집, 공유기 갯수
coordinate = []
for _ in range(N): # 집의 좌표
    coordinate.append(int(sys.stdin.readline().split()[0]))
coordinate.sort()


# 임의로 distance(거리) 값을 정한 후 공유기를 설치한다.
# 설치한 공유기 갯수를 반환하고 그 결과를 통해 이진 탐색 범위 결정에 활용.
def install_wifi(distance):
    current = coordinate[0]
    cnt = 1
    for i in range(1, N):
        if coordinate[i] >= current + distance:
            current = coordinate[i]
            cnt += 1
    return cnt


answer = 0
left, right = 0, coordinate[-1]
while left <= right:
    mid = (left + right) // 2
    count = install_wifi(mid)
    if count < C:
        right = mid - 1
    else:
        left = mid + 1
        answer = mid
print(answer)