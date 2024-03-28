N = int(input())

# 육각형 이동 방법 -> 육각형을 좀 길게 늘림
# 이동 순서 고려
dx = [0, 1, 1, 0, -1, -1]
dy = [1, 1, -1, -1, -1, 1]

answer = 0


# 몇번 회전, 직전에 사용한 방향, 방문 좌표, 현재 좌표
def dfs(n, dir_num, visited, now_loc):
    global answer

    # 현재 좌표를 이미 방문했다면
    if now_loc in visited:
        # N 번 회전했다면
        if n == N:
            answer += 1
        return
    # backtracking
    if n > N:
        return

    visited.append(now_loc)

    new_loc1 = (now_loc[0] + dx[(dir_num + 1) % 6], now_loc[1] + dy[(dir_num + 1) % 6])
    new_loc2 = (now_loc[0] + dx[(dir_num - 1) % 6], now_loc[1] + dy[(dir_num - 1) % 6])

    dfs(n + 1, (dir_num + 1) % 6, visited, new_loc1)
    dfs(n + 1, (dir_num - 1) % 6, visited, new_loc2)

    visited.pop()


dfs(0, 0, [(0, 0)], (0, 1))
print(answer)

# 위 코드를 통해서 미리 답을 구해두고 정답 출력
ans = [0, 0, 0, 0, 0, 2, 2, 4, 8, 26, 36, 80, 148, 332, 556, 1172,
       2112, 4350, 7732, 15568, 28204, 56100, 101640]
print(ans[N])