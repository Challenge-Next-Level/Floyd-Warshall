N, D = map(int, input().split())

short_load_list = list()
for _ in range(N):
    s, e, c = map(int, input().split())
    short_load_list.append([s, e, c])

distance = [i for i in range(D + 1)]

for i in range(D + 1):
    if i > 0:
        # 최단 거리 업데이트
        distance[i] = min(distance[i], distance[i - 1] + 1)

    # 지름길에 따른 최단 거리 업데이트
    for start, end, cost in short_load_list:
        if i == start and end <= D and distance[i] + cost < distance[end]:
            distance[end] = distance[start] + cost

print(distance[D])