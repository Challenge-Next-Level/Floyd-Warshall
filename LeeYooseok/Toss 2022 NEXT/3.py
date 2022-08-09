# 통과
def s(k, num, visited, dungeons):
    global answer
    chk = False
    for idx in range(len(dungeons)):
        if not visited[idx]:
            _d = dungeons[idx]
            if _d[0] <= k:
                visited[idx] = True
                s(k - _d[1], num + 1, visited, dungeons)
                visited[idx] = False
                chk = True
    if not chk:
        answer = max(answer, num)
        return


def solution(k, dungeons):
    global answer
    answer = 0
    s(k, 0, [False for _ in range(len(dungeons))], dungeons)
    return answer




print(solution(80, [[80, 20], [50, 40], [30, 10]]))