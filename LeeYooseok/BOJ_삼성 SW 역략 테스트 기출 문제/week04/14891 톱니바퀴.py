# 서로 맞닿은 부분이 같으면, 회전하지 않는다.
# 회전하기 이전에, 다음 톱니바퀴와의 관계를 확인해야함
# 서로 맞닿은 부분이 다르면, 반대 방향으로 회전한다.

# 회전
def rotate(n, d):
    global ns

    same_ns = list()
    # 현재 같은 극을 갖는 톱니 바퀴 확인
    for i in range(3):
        if ns[i][2] == ns[i + 1][6]:
            same_ns.append([i, i + 1])

    # n번 톱니바퀴의 왼쪽 확인
    for i in range(n - 1):
        if [n - i - 2, n - i - 1] in same_ns:
            break

        # n-i-2 번째 톱니바퀴 회전
        if i % 2 == 0:
            new_d = d * -1
        else:
            new_d = d

        if new_d == 1:
            temp = ns[n - i - 2].pop()
            ns[n - i - 2].insert(0, temp)
        else:
            temp = ns[n - i - 2].pop(0)
            ns[n - i - 2].append(temp)

    # n번 톱니바퀴의 오른쪽 확인
    for i in range(4 - n):
        if [n - i - 1, n - i] in same_ns:
            break

        # n+i 번째 톱니바퀴 회전
        if i % 2 == 0:
            new_d = d * -1
        else:
            new_d = d

        if new_d == 1:
            temp = ns[n + i].pop()
            ns[n + i].insert(0, temp)
        else:
            temp = ns[n + i].pop(0)
            ns[n + i].append(temp)

    # n번 톱니바퀴 회전
    if d == 1:
        temp = ns[n - 1].pop()
        ns[n - 1].insert(0, temp)
    else:
        temp = ns[n - 1].pop(0)
        ns[n - 1].append(temp)


# 톱니바퀴의 상태
ns = [list(map(int, input())) for _ in range(4)]

# 회전 횟수
k = int(input())

for _ in range(k):
    n, d = map(int, input().split())
    rotate(n, d)

# 점수 확인
print(ns[0][0] + 2 * ns[1][0] + 4 * ns[2][0] + 8 * ns[3][0])
