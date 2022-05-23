import sys

input = sys.stdin.readline

N, L, R = map(int, input().split())
num_people = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

while True:

    flag = False

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[j][i] == 0:
                # 연합 국가 확인
                temp = [[i, j]]
                visited[j][i] = 1
                sum_people = 0
                countries = []

                while temp:
                    now_x, now_y = temp.pop(0)
                    sum_people += num_people[now_y][now_x]
                    countries.append([now_x, now_y])

                    for k in range(4):
                        new_x, new_y = now_x + dx[k], now_y + dy[k]

                        if not (0 <= new_x < N) or not (0 <= new_y < N):
                            continue

                        if visited[new_y][new_x] == 1:
                            continue

                        diff_people = abs(num_people[now_y][now_x] - num_people[new_y][new_x])
                        if L <= diff_people <= R:
                            flag = True
                            temp.append([new_x, new_y])
                            visited[new_y][new_x] = 1

                # 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
                temp_people = int(sum_people / len(countries))
                for c in countries:
                    num_people[c[1]][c[0]] = temp_people

    if not flag:
        break
    else:
        result += 1
print(result)
