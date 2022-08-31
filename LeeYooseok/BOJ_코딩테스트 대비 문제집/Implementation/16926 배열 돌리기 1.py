import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

input_array = list()
for _ in range(N):
    input_array.append(list(map(int, input().split())))

for _ in range(R):
    temp_array = [item[:] for item in input_array]
    # 밖에서부터 돌리기
    for idx in range(min(M, N) // 2):
        s_x, e_x, s_y, e_y = idx, M - idx - 1, idx, N - idx - 1

        # 위
        for u_idx in range(s_x, e_x):
            temp_array[s_y][u_idx] = input_array[s_y][u_idx + 1]

        # 오른쪽
        for r_idx in range(s_y, e_y):
            temp_array[r_idx][e_x] = input_array[r_idx + 1][e_x]

        # 아래
        for d_idx in range(e_x, s_x, -1):
            temp_array[e_y][d_idx] = input_array[e_y][d_idx - 1]

        # 왼쪽
        for l_idx in range(e_y, s_y, -1):
            temp_array[l_idx][s_x] = input_array[l_idx - 1][s_x]

    input_array = [item[:] for item in temp_array]

for row in input_array:
    print(" ".join(list(map(str, row))))
