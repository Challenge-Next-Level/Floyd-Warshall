from collections import deque

def solution(k, dungeons):
    answer = 0
    queue = deque()
    visited = [False for _ in range(len(dungeons))]
    for idx in range(len(dungeons)):
        dungeon = dungeons[idx]
        if dungeon[0] <= k:
            visited[idx] = True
            queue.append([visited[:], k - dungeon[1], 1])
            visited[idx] = False
            answer = 1

    while queue:
        now_visited, remain_k, cnt = queue.popleft()

        if answer < cnt:
            answer = cnt

        for idx in range(len(dungeons)):
            dungeon = dungeons[idx]
            if not now_visited[idx] and dungeon[0] <= remain_k:
                now_visited[idx] = True
                queue.append([now_visited[:], remain_k - dungeon[1], cnt + 1])
                now_visited[idx] = False

    return answer
