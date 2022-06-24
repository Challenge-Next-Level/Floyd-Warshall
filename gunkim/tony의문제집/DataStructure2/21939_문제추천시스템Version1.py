import sys
import heapq

n = int(input())
idx = 0
visited = [False for _ in range(n)]
minHeap = []
maxHeap = []
dict = {}
for _ in range(n):
    num, dif = map(int, sys.stdin.readline().split())
    heapq.heappush(minHeap, [dif, num, idx])
    heapq.heappush(maxHeap, [-dif, -num, idx])
    dict[num] = idx
    idx += 1
m = int(input())
for _ in range(m):
    case = list(sys.stdin.readline().split())
    while minHeap and visited[minHeap[0][2]]:
        heapq.heappop(minHeap)
    while maxHeap and visited[maxHeap[0][2]]:
        heapq.heappop(maxHeap)
    if case[0] == 'add':
        heapq.heappush(minHeap, [int(case[2]), int(case[1]), idx])
        heapq.heappush(maxHeap, [-int(case[2]), -int(case[1]), idx])
        dict[int(case[1])] = idx
        visited.append(False)
        idx += 1
    elif case[0] == 'solved':
        visited[dict[int(case[1])]] = True
    elif case[0] == 'recommend':
        if case[1] == '1' and maxHeap:
            visited[maxHeap[0][2]] = True
            print(-maxHeap[0][1])
        elif case[1] == '-1' and minHeap:
            visited[minHeap[0][2]] = True
            print(minHeap[0][1])