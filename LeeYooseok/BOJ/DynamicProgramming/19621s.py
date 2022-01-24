n = int(input())

meets = list()

# 마지막 시작 값
last_start = 0

for _ in range(n):
    meet = list(map(int, input().split()))
    meets.append(meet)
    last_start = max(last_start, meet[0])

meets.sort()

# 결과 담을 리스트
result = list()


# i = 현재 회의, current = 이전 회의까지의 총 인원수
def bfs(i, current):
    # 현재 회의
    meet = meets[i]
    # 이전 회의까지의 총 인원수 + 현재 회의의 인원수
    current += meet[2]

    # 현재 회의가 마지막 회의인지 확인 - 현재 회의 종료 > 마지막 회의 시작
    if meet[1] > last_start:
        result.append(current)
        return

    # 다음 회의 확인
    for j in range(i + 1, n):
        # 다음 회의가 가능한지 확인 - 현재 회의 종료 > 다음 회의 시작
        if meet[1] > meets[j][0]:
            continue
        else:
            bfs(j, current)


for i in range(n):
    bfs(i, 0)

print(max(result))
