import heapq

N, M, K = map(int, input().split())

group_list = [list() for _ in range(M + 1)]
header_group = list()

for idx in range(1, N + 1):
    new_line = idx % M
    if new_line == 0:
        new_line = M
    D, H = map(int, input().split())

    if idx <= M:
        heapq.heappush(header_group, [-1 * D, -1 * H, new_line, idx])
    else:
        group_list[new_line].append([-1 * D, -1 * H, new_line, idx])

answer = 0
while header_group:
    now_people = heapq.heappop(header_group)

    if now_people[3] == K + 1:
        print(answer)
        exit()

    answer += 1

    if group_list[now_people[2]]:
        heapq.heappush(header_group, group_list[now_people[2]].pop(0))

