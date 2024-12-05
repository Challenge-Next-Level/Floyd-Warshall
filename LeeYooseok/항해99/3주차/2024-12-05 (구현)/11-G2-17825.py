# 각 칸에서 얻을 수 있는 점수
point_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35]

# 각 칸에서 이동할 수 있는 칸
graph = {
    0: [1],  # 시작 칸
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: [6, 21],
    6: [7],
    7: [8],
    8: [9],
    9: [10],
    10: [11, 24],
    11: [12],
    12: [13],
    13: [14],
    14: [15],
    15: [16, 26],
    16: [17],
    17: [18],
    18: [19],
    19: [20],
    20: [-1],  # 마지막 칸
    21: [22],
    22: [23],
    23: [29],
    24: [25],
    25: [29],
    26: [27],
    27: [28],
    28: [29],
    29: [30],
    30: [31],
    31: [20]
}

dice_list = list(map(int, input().split()))

stack = list()
# [현재 말의 위치, 주사위 차례, 획득 점수
stack.append([[0, 0, 0, 0], 0, 0])

answer = 0

while stack:
    now_loc_list, dice_idx, now_score = stack.pop()

    # 종료 조건
    if dice_idx == 10:
        answer = max(answer, now_score)
        continue

    # 현재 주사위
    now_move = dice_list[dice_idx]

    # 4개의 말에 대해서
    for i in range(4):
        now_loc = now_loc_list[i]

        # 현재 말이 마지막 칸에 있다면,
        if now_loc == -1:
            continue

        # 현재 말 now_move 만큼 이동
        for j in range(now_move):
            # 만약 출발 칸이 파란색 칸이면
            if j == 0 and len(graph[now_loc]) == 2:
                now_loc = graph[now_loc][1]
            else:
                now_loc = graph[now_loc][0]

            # 도착 칸에 있다면 이동을 종료한다.
            if now_loc == -1:
                break

        # 도착 칸에 다른 말이 있다면
        if now_loc != -1 and now_loc in now_loc_list:
            continue

        # 점수 획득
        add_score = 0
        if now_loc != -1:
            add_score = point_list[now_loc]

        # 다음 탐색 진행
        new_loc_list = now_loc_list[:]
        new_loc_list[i] = now_loc
        stack.append([new_loc_list, dice_idx + 1, now_score + add_score])

print(answer)