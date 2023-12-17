N = int(input())
stone_list = [0]
stone_list.extend(list(map(int, input().split())))


def check_able(K):
    visited = [True, True]

    for j in range(2, N + 1):
        able_to_j = False
        for i in range(1, j):
            # i로 올 수 있는지 확인
            if not visited[i]:
                continue

            # i 에서 j 로 넘어갈때
            need_power = (j - i) * (1 + abs(stone_list[i] - stone_list[j]))

            # 힘이 K 이상 필요하면 못건넘
            if need_power > K:
                continue

            able_to_j = True
            pass

        visited.append(able_to_j)

    return visited[N]


left, right = 0, (N - 1) * (1 + abs(stone_list[1] - stone_list[N]))
answer = right

while left <= right:
    mid = (left + right) // 2

    if check_able(mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)
