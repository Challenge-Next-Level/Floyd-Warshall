import heapq

n = int(input())
timeTable = list()
for _ in range(n):
    s, e = map(int, input().split())
    timeTable.append([s, e])

# 시작 시간 기준으로 정렬
timeTable.sort(key=lambda x: x[0])

answer = 1

h = [0]

for _s, _e in timeTable:
    # 현재 회의 시작 시간과, 일정의 가장 마지막 회의의 종료 시간 비교
    if _s >= h[0]:
        heapq.heappop(h)
    else:
        answer += 1
    # 일정의 가장 마지막 종료 시간 update
    heapq.heappush(h, _e)

print(answer)
