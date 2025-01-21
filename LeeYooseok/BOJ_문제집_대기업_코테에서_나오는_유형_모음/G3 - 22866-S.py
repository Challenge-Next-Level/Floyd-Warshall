N = int(input())
building_list = list(map(int, input().split()))

answer = [[0, -1e9] for _ in range(N)]

stack = list()
for i in range(N):
    now_building = building_list[i]
    # stack 에 now_building 보다 작거나 같은 것 들은 다 pop
    while stack and building_list[stack[-1]] <= now_building:
        stack.pop()

    if stack:
        answer[i][0] += len(stack)
        answer[i][1] = stack[-1]
    stack.append(i)

stack = list()
for i in range(N - 1, -1, -1):
    now_building = building_list[i]
    while stack and building_list[stack[-1]] <= now_building:
        stack.pop()

    if stack:
        answer[i][0] += len(stack)
        if stack[-1] - i < i - answer[i][1]:
            answer[i][1] = stack[-1]
    stack.append(i)

for i in range(N):
    if answer[i][0] != 0:
        print(answer[i][0], answer[i][1] + 1)
    else:
        print(0)