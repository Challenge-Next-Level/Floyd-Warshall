xs, ys = map(int, input().split())
xe, ye = map(int, input().split())

# 1. 플로이드 워셜을 위한 graph 생성
# 시작점, 텔레포트 3쌍 (각 2개씩), 끝점 -> 총 8개의 포인트
graph = [[1e9 for _ in range(8)] for _ in range(8)]

# 2. 자기 자신에서 자기 자신으로 가는 비용 초기화
for i in range(8):
    graph[i][i] = 0

# 3. 인덱스 정보 입력용 딕셔너리 생성
# 시작점 인덱스 : 0, 끝점 인덱스 : 7
dic = dict()
dic[0], dic[7] = (xs, ys), (xe, ye)

# 4. 텔레포트 정보 입력
for i in range(1, 7, 2):
    x1, y1, x2, y2 = map(int, input().split())

    dic[i], dic[i + 1] = (x1, y1), (x2, y2)

    # graph 에 기본 이동, 텔레포트 이동 중 작은 값 입력
    jump = abs((x2 - x1)) + abs((y2 - y1))
    graph[i][i + 1] = min(10, jump)
    graph[i + 1][i] = min(10, jump)

# 5. 텔레포트가 불가능한 지역은 점프로 이동하는 거리 입력
for i in range(8):
    for j in range(8):
        if graph[i][j] == 1e9:
            graph[i][j] = abs(dic[i][0] - dic[j][0]) + abs(dic[i][1] - dic[j][1])

# 6. 플루이드-워셜 알고리즘 수행
graph[0][7], graph[7][0] = abs((xe - xs)) + abs((ye - ys)), abs((xe - xs)) + abs((ye - ys))
for k in range(8):
    for i in range(8):
        for j in range(8):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 7. 결과 출력
print(graph[0][7])
