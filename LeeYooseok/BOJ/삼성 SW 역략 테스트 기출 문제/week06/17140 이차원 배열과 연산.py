# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.

#수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
# 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다.
# 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.

r, c, k = map(int, input().split())

A_board = [[0] * 100 for _ in range(100)]
for i in range(3):
    input_list = list(map(int, input().split()))
    for j in range(3):
        A_board[i][j] = input_list[j]

now_r, now_c = 3, 3

result = 0

while A_board[r][c] != k and result <= 100:
    result += 1
    new_A_board = list()
    temp_A_board = list()
    temp_r, temp_c = 0, 0

    # C 연산 수행
    if now_r < now_c:
        temp_r, temp_c = now_c, now_r
        for _c in range(c):
            temp = list()
            for _r in range(r):
                temp.append(A_board[_r][_c])

            temp_A_board.append(temp)
    else:
        temp_r, temp_c = now_r, now_c
        temp_A_board = [item[:] for item in A_board]

    # 정렬 수행
    for __r in range(temp_r):
        new_list = dict()
        now_list = temp_A_board[__r]
        for num in now_list:
            if not new_list[num]:
                new_list[num] = 1
            else:
                new_list += 1


        sorted(new_list.items(), key=lambda x: x[1])