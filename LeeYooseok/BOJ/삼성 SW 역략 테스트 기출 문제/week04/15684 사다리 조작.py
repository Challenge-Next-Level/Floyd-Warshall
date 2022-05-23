# 시간초과
# 세로선 개수, 가로선 개수, 세로선 마다 가로선을 놓을 수 있는 위치의 개수
# 실제 보드 판 크기 : n X h
import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

graph = [[] for _ in range(n + 1)]

flag = False
result = 4

for _ in range(m):
    # 높이 a 에 b -> b+1로 가는 가로선 있음
    a, b = map(int, input().split())
    graph[b].append(a)


def able_check(checked_graph):
    for i in range(1, n + 1):
        k = i
        for j in range(1, h+1):
            if k > n:
                break
            if checked_graph[k]:
                if j in checked_graph[k]:
                    k += 1
                    continue
            if checked_graph[k-1]:
                if k > 0 and j in checked_graph[k - 1]:
                    k -= 1
                    continue
        if k != i:
            return False
    return True


def check(cnt, start_x, start_y, graph):
    global result, flag
    if cnt >= result:
        return
    else:
        # 가능한지 확인
        if able_check(graph):
            flag = True
            result = min(result, cnt)
            if result <= 3:
                print(result)
                exit()
            return

        # 길 추가
        for i in range(start_x, n-1):
            for j in range(start_y, h):

                if j + 1 in graph[i + 1]:
                    continue
                graph[i + 1].append(j + 1)

                if j == h - 1:
                    check(cnt + 1, start_x + 1, 0, graph)
                else:
                    check(cnt + 1, start_x, start_y + 1, graph)

                graph[i + 1].pop()


check(0, 0, 0, graph)

if flag:
    if result > 3:
        print(-1)
    else:
        print(result)
else:
    print(-1)