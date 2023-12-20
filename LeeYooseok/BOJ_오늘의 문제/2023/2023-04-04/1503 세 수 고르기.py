N, S = map(int, input().split())
if S == 0:
    print(0)
    exit()
s_set = set(list(map(int, input().split())))

num_set = set(list(i for i in range(1, 1002)))
num_set -= s_set
num_list = list(num_set)
len_num_list = len(num_list)

answer = 1e9


def dfs(num, n, idx):
    global answer
    if n == 3:
        answer = min(answer, abs(N - num))
        return

    for next_idx in range(idx, len_num_list):
        next_num = num * num_list[next_idx]
        if next_num > N:
            if (next_num - N) < answer:
                dfs(next_num, n + 1, next_idx)
        else:
            dfs(next_num, n + 1, next_idx)

dfs(1, 0, 0)
print(answer)
