N = int(input())
tower_list = list(map(int, input().split()))

stack = []
answer = [0 for _ in range(N)]

for i in range(N):
    while stack:
        if stack[-1][1] >= tower_list[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            # stack 에는 현재 탑보다 높은 탑만 존재하게 한다.
            # 현재 탑보다 낮은 탑은 탐색할 가치가 없으므로
            stack.pop()
    stack.append([i, tower_list[i]])

print(*answer)