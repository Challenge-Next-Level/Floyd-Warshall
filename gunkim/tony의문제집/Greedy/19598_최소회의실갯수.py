# 11000(강의실배정) 문제랑 그냥 같다 ㅜㅜ 코드 그냥 그대로 복붙했다.
import sys
import heapq # 가장 빨리 끝나는 회의를 알고 싶었기에 heapq 사용(시간초과 방지)

n = int(input())
room = [0]
heap = []
heapq.heappush(heap, [0, 0]) # 종료시간, room index

case = []
for _ in range(n): # 회의 시작 시간이 정렬된 상태로 입력되지 않을 수 있어서 입력을 따로 받는다
    case.append(list(map(int, sys.stdin.readline().split())))
case.sort() # 시작 시간 순서로 정렬

for c in range(n):
    start, end = case[c]
    if heap[0][0] <= start: # 비는 회의실이 있다면
        time, index = heapq.heappop(heap)
        room[index] = end
        heapq.heappush(heap, [end, index])
    else: # 없다면 새로 회의실 추가
        room.append(end)
        heapq.heappush(heap, [end, len(room) - 1])
print(len(room))