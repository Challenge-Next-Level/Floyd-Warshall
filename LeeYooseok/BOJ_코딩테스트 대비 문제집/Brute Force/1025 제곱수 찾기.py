import math

N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
answer = -1

for n in range(N): # 어느 행에서 시작할 것인가?
    for m in range(M): # 어느 열에서 시작할 것인가?
        for dif_n in range(-N, N): # 행에서의 공차,-M 부터 시작
            for dif_m in range(-M, M): # 열에서의 공차, -N 부터 시작
                # 두 공차가 0이면 무한 루프
                if dif_m == 0 and dif_n == 0:
                    continue

                step = 0
                y = n # 현재 행
                x = m # 현재 열
                value = ''

                # 입력받은 수들의 범위 안에서 가능한 수열 추출
                while (0 <= y < N) and (0 <= x < M):
                    # 숫자 조합
                    value += str(board[y][x])
                    step += 1

                    # 제곱수 이고, 최댓값 갱신이 가능한지 확인
                    value_int = int(value)
                    value_sqrt = math.sqrt(value_int)
                    value_decimal = value_sqrt - int(value_sqrt)

                    if value_decimal == 0:
                        answer = max(value_int, answer)

                    y = n + step * dif_n
                    x = m + step * dif_m

print(answer)