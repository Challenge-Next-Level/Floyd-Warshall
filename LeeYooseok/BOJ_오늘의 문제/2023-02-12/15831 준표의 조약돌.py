N, B, W = map(int, input().split())
stone_list = list(input())

prefix_sum_B = [0]
prefix_sum_W = [0]
for stone in stone_list:
    if stone == 'B':
        prefix_sum_B.append(prefix_sum_B[-1] + 1)
        prefix_sum_W.append(prefix_sum_W[-1])
    else:
        prefix_sum_W.append(prefix_sum_W[-1] + 1)
        prefix_sum_B.append(prefix_sum_B[-1])

answer = 0

for start in range(N):
    for end in range(start, N):
        # 검정색 개수
        cnt_Black = prefix_sum_B[end + 1] - prefix_sum_B[start]
        cnt_White = prefix_sum_W[end + 1] - prefix_sum_W[start]

        if cnt_Black <= B and cnt_White >= W:
            answer = max(answer, end - start + 1)
print(answer)
