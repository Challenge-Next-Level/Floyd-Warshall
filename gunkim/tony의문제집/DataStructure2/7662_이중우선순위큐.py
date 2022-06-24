# visited를 활용해서 해당 숫자를 pop했는지 체크를 할 수 있음. 좋은 아이디어 같다.
import sys
import heapq
from collections import deque

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap = []
    max_heap = []
    visited = [False for _ in range(k)] # 방문 표시를 통해 heap에서 pop을 하기 위함
    for idx in range(k):
        case = list(sys.stdin.readline().split())
        ch = case[0] # 문자
        n = int(case[1]) # 숫자

        if ch == 'I':
            heapq.heappush(min_heap, [n, idx])
            heapq.heappush(max_heap, [-n, idx])
        elif ch == 'D':
            while min_heap and visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            while max_heap and visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if n == 1 and max_heap:
                visited[max_heap[0][1]] = True
            elif n == -1 and min_heap:
                visited[min_heap[0][1]] = True
    while min_heap and visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(str(-max_heap[0][0]) + ' ' + str(min_heap[0][0]))
