from collections import deque

N, M = map(int, input().split())

num_list = deque(list(i for i in range(1, N + 1)))

hope_num_list = list(map(int, input().split()))
hope_num_list = deque(hope_num_list)

answer = 0

while hope_num_list:
    hope_num = hope_num_list[0]
    hope_num_idx = num_list.index(hope_num)

    if hope_num_idx <= (len(num_list) - hope_num_idx):
        num_list.rotate(-1 * hope_num_idx)
        answer += hope_num_idx
    else:
        num_list.rotate(len(num_list) - hope_num_idx)
        answer += (len(num_list) - hope_num_idx)
    hope_num_list.popleft()
    num_list.popleft()

print(answer)