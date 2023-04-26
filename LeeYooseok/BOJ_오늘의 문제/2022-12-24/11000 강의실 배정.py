import heapq

N = int(input())
class_list = list()
for _ in range(N):
    s, t = map(int, input().split())
    class_list.append([s, t])

# 시작 시간 기준 정렬
class_list.sort()

# 단, 이 때 종료시간이 빠른 회의실부터 다음 회의를 이어서 개최해야 하기 때문에
# 우선순위 큐를 이용해 큐에 push를 해주어 큐가 정렬상태를 유지할 수 있도록 해준다.
room = list()
heapq.heappush(room, class_list[0][1])

for i in range(1, N):
    if class_list[i][0] < room[0]:
        # 새로운 방 개설
        heapq.heappush(room, class_list[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, class_list[i][1])

print(len(room))
