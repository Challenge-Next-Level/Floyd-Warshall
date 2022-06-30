
import sys
import heapq

n = int(input())
idx = 0
visited = [False for _ in range(n)]
minHeap = []
maxHeap = []
divisionMinHeap = [[] for _ in range(101)]
divisionMaxHeap = [[] for _ in range(101)]
difficultyMinHeap = [[] for _ in range(101)]
difficultyMaxHeap = [[] for _ in range(101)]
dict = {}
for _ in range(n):
    P, L, G = map(int, sys.stdin.readline().split()) # 문제번호, 난이도, 알고리즘분류
    heapq.heappush(minHeap, [L, P, idx])
    heapq.heappush(maxHeap, [-L, -P, idx])
    heapq.heappush(divisionMinHeap[G], [L, P, idx])
    heapq.heappush(divisionMaxHeap[G], [-L, -P, idx])
    heapq.heappush(difficultyMinHeap[L], [P, idx])
    heapq.heappush(difficultyMaxHeap[L], [-P, idx])
    dict[P] = idx
    idx += 1
m = int(input())
for _ in range(m):
    case = list(sys.stdin.readline().split())
    if case[0] == 'add': # add P L G
        P, L, G = int(case[1]), int(case[2]), int(case[3])
        heapq.heappush(minHeap, [L, P, idx])
        heapq.heappush(maxHeap, [-L, -P, idx])
        heapq.heappush(divisionMinHeap[G], [L, P, idx])
        heapq.heappush(divisionMaxHeap[G], [-L, -P, idx])
        heapq.heappush(difficultyMinHeap[L], [P, idx])
        heapq.heappush(difficultyMaxHeap[L], [-P, idx])
        dict[P] = idx
        visited.append(False)
        idx += 1
    elif case[0] == 'solved': # solved P
        visited[dict[int(case[1])]] = True
    elif case[0] == 'recommend': # recommend G x
        G = int(case[1])
        if case[2] == '1' and divisionMaxHeap[G]:
            while divisionMaxHeap[G] and visited[divisionMaxHeap[G][0][2]]:
                heapq.heappop(divisionMaxHeap[G])
            print(-divisionMaxHeap[G][0][1])
        elif case[2] == '-1' and divisionMinHeap[G]:
            while divisionMinHeap[G] and visited[divisionMinHeap[G][0][2]]:
                heapq.heappop(divisionMinHeap[G])
            print(divisionMinHeap[G][0][1])
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
        index = int(case[2]) # 난이도
        if case[1] == '1':
            while index < 101:
                while difficultyMinHeap[index] and visited[difficultyMinHeap[index][0][1]]:
                    heapq.heappop(difficultyMinHeap[index])
                if len(difficultyMinHeap[index]) == 0:
                    index += 1
                else:
                    break
            if index > 100:
                print(-1)
            else:
                print(difficultyMinHeap[index][0][0])
        elif case[1] == '-1':
            while index > 0:
                while difficultyMaxHeap[index] and visited[difficultyMaxHeap[index][0][1]]:
                    heapq.heappop(difficultyMaxHeap[index])
                if len(difficultyMaxHeap[index]) == 0:
                    index -= 1
                else:
                    break
            if index < 1:
                print(-1)
            else:
                print(-difficultyMaxHeap[index][0][0])