import sys

input = sys.stdin.readline

N = int(input())
building_list = list(map(int, input().split()))

answer = [[0, -1e9] for _ in range(N)]

# 건물보다 왼쪽
stack = list()
for i in range(N):
    # 현재 stack 중에서 나보다 작은 건물은 pop
    while stack and building_list[stack[-1]] <= building_list[i]:
        stack.pop()

    # stack 에 남아있는 건물 -> 내가 왼쪽으로 볼 수 있는 건물 리스트
    answer[i][0] += len(stack)
    if stack:
        answer[i][1] = stack[-1] # 왼쪽으로 보이는 건물 중 가장 가까운 건물
    # i + 1의 왼쪽부터 차례대로 stack 에 넣어짐
    stack.append(i)

# 건물보다 오른쪽
stack = list()
for i in range(N - 1, -1, -1):
    # 현재 stack 중에서 나보다 작은 건물은 pop
    while stack and building_list[stack[-1]] <= building_list[i]:
        stack.pop()

    # stack 에 남아있는 건물 -> 내가 오른쪽으로 볼 수 있는 건물 리스트
    answer[i][0] += len(stack)
    if stack and stack[-1] - i < i - answer[i][1]:
        answer[i][1] = stack[-1]  # 왼쪽으로 보이는 건물 중 가장 가까운 건물
    # i + 1의 왼쪽부터 차례대로 stack 에 넣어짐
    stack.append(i)

for i in range(N):
    if answer[i][0] != 0:
        print(answer[i][0], answer[i][1] + 1)
    else:
        print(0)
