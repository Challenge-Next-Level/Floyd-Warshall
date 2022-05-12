# 길 하나씩 확인

n, l = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

result = 0


def check(road):
    visited = [0] * n
    for i in range(len(road) - 1):
        # 다음 길로 지나갈 수 있으면
        if road[i] == road[i + 1]:
            continue
        # 다음 길의 높이가 더 높으면
        elif road[i+1] > road[i]:
            # 높이가 1 이상 차이나면,
            if road[i+1] != road[i] + 1:
                return False
            else:
                # 지름길 놓을 수 있는지 확인
                # 충분한 공간이 나오는지 확인
                if i + 1 < l:
                    return False
                else:
                    # 이전 길의 높낮이가 다르면
                    h = road[i]
                    for l_ in range(l):
                        if h != road[i-l_] or visited[i-l_] == 1:
                            return False
                    # 경사로 놓음
                    for l_ in range(l):
                        visited[i-l_] = 1
        # 다음 길의 높이가 더 낮으면
        else:
            if road[i+1] + 1 != road[i]:
                return False
            else:
                if i+l >= n:
                    return False
                else:
                    h = road[i+1]
                    for l_ in range(l):
                        if h != road[i+1+l_] or visited[i+1+l_] == 1:
                            return False
                    for l_ in range(l):
                        visited[i+1+l_] = 1
    return True


# 가로 길 확인
for r in board:
    if check(r):
        result += 1

# 세로 길 확인
for i in range(n):
    r = list()
    for j in range(n):
        r.append(board[j][i])
    if check(r):
        result += 1

print(result)
