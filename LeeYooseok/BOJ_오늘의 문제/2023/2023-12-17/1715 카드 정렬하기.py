# 우선 순위 큐
# 1. 우선 순위 큐에 모든 카드 개수를 넣는다.
# 2. 우선 순위 큐에서 가장 작은 수 2개를 pop 해서 더한다.
# 3. 더한 수를 우선 순위 큐에 넣는다.
# 4. 2 ~ 3 을 큐가 비어있을 때까지 반복한다.

import heapq

N = int(input())
num_cards = list()
for _ in range(N):
    heapq.heappush(num_cards, int(input()))

answer = 0

while len(num_cards) >= 2:
    a = heapq.heappop(num_cards)
    b = heapq.heappop(num_cards)

    answer += (a + b)

    heapq.heappush(num_cards, a + b)

print(answer)