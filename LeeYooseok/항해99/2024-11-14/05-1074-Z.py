N, r, c = map(int, input().split())


def solve(n, now_y, now_x, now_value):
    if n == 1:
        if now_y == 0 and now_x == 0:
            print(now_value)
        elif now_y == 0 and now_x == 1:
            print(now_value + 1)
        elif now_y == 1 and now_x == 0:
            print(now_value + 2)
        else:
            print(now_value + 3)

    else:
        # 현재 단계에서 (now_x, now_y)의 위치에 따라서 다음 함수 실행 구역이 정해짐
        if 0 <= now_y < (2 ** (n - 1)) and 0 <= now_x < (2 ** (n - 1)):
            solve(n - 1, now_y, now_x, now_value)
        elif 0 <= now_y < (2 ** (n - 1)) and (2 ** (n - 1)) <= now_x:
            solve(n - 1, now_y, now_x - (2 ** (n - 1)), now_value + ((2 ** (n - 1)) ** 2))
        elif (2 ** (n - 1)) <= now_y and 0 <= now_x < (2 ** (n - 1)):
            solve(n - 1, now_y - (2 ** (n - 1)), now_x, now_value + 2 * ((2 ** (n - 1)) ** 2))
        else:
            solve(n - 1, now_y - (2 ** (n - 1)), now_x - (2 ** (n - 1)), now_value + 3 * ((2 ** (n - 1)) ** 2))


solve(N, r, c, 0)
