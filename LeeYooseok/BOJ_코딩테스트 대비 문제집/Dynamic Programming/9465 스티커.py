T = int(input())

for _ in range(T):
    n = int(input())
    s_list = list()
    s_list.append(list(map(int, input().split())))
    s_list.append(list(map(int, input().split())))

    for j in range(1, n):
        # j 가 1 일때, j가 0이고 대각선에 위치한 스티커를 사용할 수 있다.
        if j == 1:
            s_list[0][j] += s_list[1][j-1]
            s_list[1][j] += s_list[0][j-1]
        # j단계 일때, j-1 단계의 대각선 위치 또는 j-2 단계의 대각선 위치 중 최댓값
        else:
            s_list[0][j] += max(s_list[1][j-1], s_list[1][j-2])
            s_list[1][j] += max(s_list[0][j-1], s_list[0][j-2])

    print(max(s_list[0][n-1], s_list[1][n-1]))

