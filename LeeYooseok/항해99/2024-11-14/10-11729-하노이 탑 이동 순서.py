N = int(input())

answer = 0
move_list = list()

def solve(n, left, mid, right):
    global answer

    # 원반이 1개라면, 그냥 left -> right 이동
    if n == 1:
        answer += 1
        move_list.append([left, right])
        return

    # 원반 n-1개를 가운데로 이동
    solve(n - 1, left, right, mid)

    # 가장 큰 원반을 목적지로 이동
    answer += 1
    move_list.append([left, right])

    # 가운데에 있는 원반 n-1개를 목적지로 이동
    solve(n - 1, mid, left, right)

solve(N, 1, 2, 3)

print(answer)
for move in move_list:
    print(*move)