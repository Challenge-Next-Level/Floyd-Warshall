N = int(input())
tower_list = list(map(int, input().split()))

answer = [0 for _ in range(N)]

stack = list()

for i in range(N):
    while stack:
        if stack[-1][1] >= tower_list[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append([i, tower_list[i]])

print(*answer)