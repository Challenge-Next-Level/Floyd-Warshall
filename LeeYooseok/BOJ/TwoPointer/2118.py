"""
두 지점 사이의 거리(시계 방향, 반 시계 방향 중 작은 값) 중 최댓값 반환
못 품
"""

n = int(input())

points = [int(input()) for _ in range(n)]
points.append(0)

total = sum(points)

start = 0
end = 0

result = 0

now = points[start]

while start <= end < n:
    minNow = min(now, total - now)

    result = max(result, minNow)

    # end를 이동시키다가 minNow가 더 이상 늘어나지 않을 경우?
    if now == minNow:
        end += 1
        now += points[end]
    else:
        now -= points[start]
        start += 1


print(result)