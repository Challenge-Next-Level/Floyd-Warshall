N, M, L, K = map(int, input().split())

point_list = list()

for _ in range(K):
    x, y = map(int, input().split())
    point_list.append([x, y])

answer = K

for a_x, a_y in point_list:
    for b_x, b_y in point_list:
        point_count = 0

        for c_x, c_y in point_list:
            if a_x <= c_x and c_x <= a_x + L and b_y <= c_y and c_y <= b_y + L:
                point_count += 1

        answer = min(answer, K - point_count)

print(answer)