# 범위 : -1010000 ~ 1010000

N = int(input())

circle = list()

for n in range(N):
    x, r = map(int, input().split())

    circle.append([x - r, n, 0]) # 원의 시작 : 좌표, 원의 번호, 열림(0)
    circle.append([x + r, n, 1]) # 원의 끝 : 좌표, 원의 번호, 닫힘(1)

circle.sort()

circle_stack = list()
for i in range(N):
    cir_flag = circle[i][2]
    # 원의 시작이면
    if cir_flag == 0:
        circle_stack.append(circle[i])
    # 원의 끝이면
    else:
        # 이전 원이 닫히지 않은 상태이면
        if circle_stack[-1][2] == 0:
            # 동일한 원이면 원 끝
            if circle_stack[-1][1] == circle[i][1]:
                circle_stack.pop()
            else:
                print("NO")
                exit()
print("YES")
