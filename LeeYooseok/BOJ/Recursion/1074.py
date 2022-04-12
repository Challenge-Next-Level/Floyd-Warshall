# size

n, r, c = map(int, input().split())


def solution(n, r, c, start):
    if n == 1:
        if r == 0 and c == 0:
            print(start)
        elif r == 1 and c == 0:
            print(start + 2)
        elif r == 0 and c == 1:
            print(start + 1)
        else:
            print(start + 3)
    else:
        # 4 구역으로 나눠야함
        if 0 <= r < (2 ** (n - 1)) and 0 <= c < (2 ** (n - 1)):
            solution(n - 1, r, c, start)
        elif (2 ** (n - 1)) <= r and 0 <= c < (2 ** (n - 1)):
            solution(n - 1, r - (2 ** (n - 1)), c, start + 2 * (2 ** (n - 1)) ** 2)
        elif 0 <= r < (2 ** (n - 1)) and (2 ** (n - 1)) <= c:
            solution(n - 1, r, c - (2 ** (n - 1)), start + ((2 ** (n - 1)) ** 2))
        else:
            solution(n - 1, r - (2 ** (n - 1)), c - (2 ** (n - 1)), start + 3 * ((2 ** (n - 1)) ** 2))


solution(n, r, c, 0)
