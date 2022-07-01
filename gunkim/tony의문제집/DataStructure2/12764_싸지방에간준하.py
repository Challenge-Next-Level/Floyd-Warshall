# python3는 시간초과 발생, pypy3환경에서 테스트 해야한다
import sys
import heapq

n = int(sys.stdin.readline())
wait = []
for _ in range(n):
    heapq.heappush(wait, list(map(int, sys.stdin.readline().split()))) # 시작시간, 끝시간

# 사이즈 정의 없이 필요할 때 마다 append 하려 했는데 그 부분 때문에 시간초과 발생
computer = [0 for _ in range(n)]
count = [0 for _ in range(n)]
needs = 0
while wait:
    start, end = heapq.heappop(wait)
    flag = 0
    for j in range(len(computer)):
        if computer[j] <= start:
            if computer[j] == 0:
                needs += 1
            computer[j] = end
            count[j] += 1
            break


print(needs)
for i in range(len(count)):
    if count[i] == 0:
        break
    print(count[i], end=' ')