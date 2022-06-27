N = int(input())

tower = list(map(int, input().split()))

# [탑의 번호, 높이] 저장
stack = list()
result = list()

for i in range(N):
    while stack:
        # 현재 탑이 수신 가능한 상태
        if stack[-1][1] > tower[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    # 수신 불가능한 상태
    if not stack:
        result.append(0)

    stack.append([i, tower[i]])

print(" ".join(map(str, result)))