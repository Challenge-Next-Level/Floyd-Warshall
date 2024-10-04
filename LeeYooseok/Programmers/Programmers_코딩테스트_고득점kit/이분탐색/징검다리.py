# rocks 에서 바위를 n개 제거
# 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return

def solution(distance, rocks, n):
    rocks.insert(0, 0)
    rocks.append(distance)
    rocks.sort()

    distances = list()
    for r in range(1, len(rocks)):
        distances.append(rocks[r] - rocks[r - 1])

    # 지점 사이의 거리가 최소인 곳을 없앤다.
    for _ in range(n):
        i = distances.index(min(distances))
        min_distance = distances[i]

        if len(distances) >= 2:
            if i == 0:
                distances = distances[1:]
                distances[0] += min_distance
            elif i == len(distances) - 1:
                distances = distances[:-1]
                distances[-1] += min_distance
            else:
                del distances[i]
                distances[i] += min_distance
    return min(distances)


print(solution(25, [2, 14, 11, 21, 17], 2))
print(solution(25, [2, 11, 14, 17, 17], 2))