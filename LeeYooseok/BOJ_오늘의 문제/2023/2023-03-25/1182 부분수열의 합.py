N, S = map(int, input().split())

num_list = list(map(int, input().split()))

answer = 0


def dfs(temp_sum, now_idx):
    global answer
    if temp_sum == S:
        answer += 1
    if now_idx == N - 1:
        return

    for next_idx in range(now_idx + 1, N):
        dfs(temp_sum + num_list[next_idx], next_idx)


for idx in range(N):
    dfs(num_list[idx], idx)

print(answer)
