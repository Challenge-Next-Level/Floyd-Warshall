def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ## 동 남 서 북 순서
            nx, ny = x + dx[i], y + dy[i]
            while True:
                ## 범위를 벗어난다
                if not (0 <= nx < n and 0 <= ny < m): break

                ## 벽을 만난다
                if board[nx][ny] == '*': break

                ## 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                if visited[nx][ny] < visited[x][y] + 1: break

                ## board업데이트, queue 추가
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx + dx[i]
                ny = ny + dy[i]