
import sys
import heapq

n = int(input())
idx = 0
visited = [False for _ in range(n)]
minHeap = []
maxHeap = []
divisionMinHeap = {}
divisionMaxHeap = {}
dict = {}
for _ in range(n):
    P, L, G = map(int, sys.stdin.readline().split()) # 문제번호, 난이도, 알고리즘분류
    heapq.heappush(minHeap, [L, P, idx])
    heapq.heappush(maxHeap, [-L, -P, idx])
    if G not in divisionMinHeap:
        divisionMinHeap[G] = []
        divisionMaxHeap[G] = []
    heapq.heappush(divisionMinHeap[G], [L, P, idx])
    heapq.heappush(divisionMaxHeap[G], [-L, -P, idx])
    dict[P] = idx
    idx += 1
m = int(input())
for _ in range(m):
    case = list(sys.stdin.readline().split())
    if case[0] == 'add':
        heapq.heappush(minHeap, [int(case[2]), int(case[1]), idx])
        heapq.heappush(maxHeap, [-int(case[2]), -int(case[1]), idx])
        if int(case[3]) not in divisionMinHeap:
            divisionMinHeap[int(case[3])] = []
            divisionMaxHeap[int(case[3])] = []
        heapq.heappush(divisionMinHeap[int(case[3])], [int(case[2]), int(case[1]), idx])
        heapq.heappush(divisionMaxHeap[int(case[3])], [-int(case[2]), -int(case[1]), idx])
        dict[int(case[1])] = idx
        visited.append(False)
        idx += 1
    elif case[0] == 'solved':
        visited[dict[int(case[1])]] = True
    elif case[0] == 'recommend': # recommend G x
        if case[2] == '1' and divisionMaxHeap[int(case[1])]:
            while divisionMaxHeap[int(case[1])] and visited[divisionMaxHeap[int(case[1])][0][2]]:
                heapq.heappop(divisionMaxHeap[int(case[1])])
            print(-divisionMaxHeap[int(case[1])][0][1])
        elif case[2] == '-1' and divisionMinHeap[int(case[1])]:
            while divisionMinHeap[int(case[1])] and visited[divisionMinHeap[int(case[1])][0][2]]:
                heapq.heappop(divisionMinHeap[int(case[1])])
            print(divisionMinHeap[int(case[1])][0][1])
    elif case[0] == 'recommend2': # recommend2 x
        if case[1] == '1' and maxHeap:
            while maxHeap and visited[maxHeap[0][2]]:
                heapq.heappop(maxHeap)
            print(-maxHeap[0][1])
        elif case[1] == '-1' and minHeap:
            while minHeap and visited[minHeap[0][2]]:
                heapq.heappop(minHeap)
            print(minHeap[0][1])
    elif case[0] == 'recommend3': # recommend3 x L
        arrayList = []
        if case[1] == '1':
            while minHeap and visited[minHeap[0][2]]:
                heapq.heappop(minHeap)
            while minHeap and minHeap[0][0] < int(case[2]):
                arrayList.append(heapq.heappop(minHeap))
            if minHeap:
                print(minHeap[0][1])
            else:
                print(-1)
            while arrayList:
                heapq.heappush(minHeap, arrayList.pop())
        elif case[1] == '-1':
            while maxHeap and visited[maxHeap[0][2]]:
                heapq.heappop(maxHeap)
            while maxHeap and -maxHeap[0][0] > int(case[2]):
                arrayList.append(heapq.heappop(maxHeap))
            if maxHeap:
                print(-maxHeap[0][1])
            else:
                print(-1)
            while arrayList:
                heapq.heappush(maxHeap, arrayList.pop())