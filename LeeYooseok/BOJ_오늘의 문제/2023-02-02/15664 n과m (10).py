N, M = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()

visited = [False] * N
answer = []


def dfs(n, idx):
    if n == M:
        print(*answer)
        return

    chk_num = 0  # 이전에 추가한 숫자와 동일하면 건너 뜀
    for i in range(idx, N):
        if not visited[i] and chk_num != num_list[i]:
            answer.append(num_list[i])
            visited[i] = True
            chk_num = num_list[i]
            dfs(n + 1, i + 1)
            answer.pop()
            visited[i] = False


dfs(0, 0)
