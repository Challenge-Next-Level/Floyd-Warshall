import heapq
from collections import defaultdict

Q = int(input())

store_dict = defaultdict(list)

answer = 0

for _ in range(Q):
    command_list = input().split()

    if command_list[0] == "1":
        name = command_list[1]
        k = command_list[2]
        value_list = command_list[3:]

        for v in value_list:
            heapq.heappush(store_dict[name], -1 * int(v))
    else:
        name = command_list[1]
        k = int(command_list[2])

        for _ in range(k):
            if not store_dict[name]:
                break

            answer += (-1 * heapq.heappop(store_dict[name]))

print(answer)
