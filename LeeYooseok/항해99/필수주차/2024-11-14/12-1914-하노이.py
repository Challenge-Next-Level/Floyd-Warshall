N = int(input())

answer = 2 ** N - 1
print(answer)

move_list = []


def solve(n, left, mid, right):
    global answer

    # n 이 1이면, 그냥 left -> right
    if n == 1:
        answer += 1
        if N <= 20:
            move_list.append([left, right])
        return

    # n-1개를 가운데로 옮긴다.
    solve(n - 1, left, right, mid)

    answer += 1
    # 가장 큰거를 left -> mid
    if N <= 20:
        move_list.append([left, right])

    # n-1개를 가운데에서 오른쪽으로 옮긴다.
    solve(n - 1, mid, left, right)


if N <= 20:
    solve(N, 1, 2, 3)
    for move in move_list:
        print(*move)