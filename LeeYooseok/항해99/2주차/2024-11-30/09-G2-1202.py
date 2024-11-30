import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())

item_list = list()
for _ in range(N):
    heapq.heappush(item_list, list(map(int, input().split())))

bag_list = sorted([int(input()) for _ in range(K)])

answer = 0

possible_item_list = list()
# 작은 가방부터 탐색한다.
for bag in bag_list:
    # bag 에 담을 수 있는 모든 item 확인
    while item_list and bag >= item_list[0][0]:
        # 가치가 높은 item 부터 넣어야 하기 때문에, 최대힙
        now_item = heapq.heappop(item_list)
        # 작은 가방에 넣을 수 있는 Item이기 때문에, 다음 가방에도 넣을 수 있는 Item이다.
        heapq.heappush(possible_item_list, [-now_item[1], now_item[0]])

    # 가방에 넣을 수 있는 Item이 있다면,
    if possible_item_list:
        # Item 을 가방에 넣는다.
        answer += -heapq.heappop(possible_item_list)[0]
    # 모든 item 을 다 넣었기 때문에?
    elif not item_list:
        break

print(answer)

