"""
- 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
- 1,2,4,8,9
"""

n, c = map(int, input().split())

home = [int(input()) for _ in range(n)]

home.sort()

result = 0

# 설치 거리 최소값, 최대값
start, end = 1, home[-1] - home[0]

while start <= end:
    mid = (start + end) // 2 # 공유기 간의 거리

    # 맨 앞집 부터 설치
    current = home[0]
    count = 1
    for i in range(1, len(home)):
        # 현재 설치된 공유기 거리를 벗어났을 시, 하나 더 설치
        if home[i] >= current + mid:
            count += 1
            current = home[i]

    # 설치된 공유기 개수 확인
    # 목표 개수보다 더 많이 설치 됬을 시
    if count >= c:
        # 거리를 늘린다.
        start = mid + 1
        result = mid # 결과 : 현재 거리?
    else:
        end = mid - 1

print(result)
