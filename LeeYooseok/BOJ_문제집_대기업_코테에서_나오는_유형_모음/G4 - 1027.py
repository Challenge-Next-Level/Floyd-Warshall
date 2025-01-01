N = int(input())

height_list = list(map(int, input().split()))


def slope(x_1, y_1, x_2, y_2):
    return (y_2 - y_1) / (x_2 - x_1)

answer = 0

# 모든 건물에 대해서 탐색한다.
for i in range(N):
    now_idx = i + 1
    now_height = height_list[i]

    # 오른쪽으로 볼 수 있는 빌딩의 수
    right_count = 0
    max_slope = None
    for candidate_i in range(i + 1, N):
        candidate_idx = candidate_i + 1
        candidate_height = height_list[candidate_i]

        now_slope = slope(now_idx, now_height, candidate_idx, candidate_height)

        if max_slope is None or max_slope < now_slope:
            max_slope = now_slope
            right_count += 1

    # 왼쪽으로 볼 수 있는 빌딩의 수
    left_count = 0
    min_slope = None
    for candidate_i in range(i - 1, -1, -1):
        candidate_idx = candidate_i + 1
        candidate_height = height_list[candidate_i]

        now_slope = slope(now_idx, now_height, candidate_idx, candidate_height)

        if min_slope is None or min_slope > now_slope:
            min_slope = now_slope
            left_count += 1

    answer = max(answer, (left_count + right_count))

print(answer)