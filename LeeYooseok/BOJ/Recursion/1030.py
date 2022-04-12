s, N, K, R1, R2, C1, C2 = map(int, input().split())

l = N ** s  # 최종 결과 한 변의 길이


def check(length, x, y):
    if length == 1:  # 한변의 길이가 1이면, 무조건 하얀색
        return 0

    border = length / N  # 현재 확인하는 사각형 한변의 길이가 length 일때, 다음에 쪼개지는 사각형 한변의 길이

    # 현재 사각형의 중심에 속해있는지 - 검정색으로 칠해야 하는지 확인
    if x >= border * (N - K) / 2 and x < border * (N + K) / 2 and y >= border * (N - K) / 2 and y < border * (N + K) / 2:
        return 1

    return check(border, x % border, y % border)

# 주어진 공간을 하나하나씩 확인
for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        print(check(l, i, j), end="")
    print()
